import json
import os
import boto3
import requests
import subprocess
from urllib.parse import unquote_plus
from flask import Flask, request, jsonify
import time
import threading

app = Flask(__name__)
s3_client = boto3.client('s3')

def process_file(record):
    source_bucket = record["s3"]["bucket"]["name"]
    source_key = unquote_plus(record["s3"]["object"]["key"])
    destination_bucket = "rag-paper-output"
    destination_key = os.path.splitext(source_key)[0] + ".mmd"
    
    print(f"Processing file: {source_bucket}/{source_key}")

    download_path = f"/tmp/{os.path.basename(source_key)}"
    s3_client.download_file(source_bucket, source_key, download_path)
    print(f"Downloaded file to {download_path}")

    file_root, file_ext = os.path.splitext(os.path.basename(source_key))
    print(f"File root: {file_root}, File extension: {file_ext}")

    output_mmd_path = f"/tmp/{file_root}.mmd"
    print(f"Output MMD path: {output_mmd_path}")

    start_time = time.time()
    try:
        result = subprocess.run(["nougat", download_path, "--out", output_mmd_path], check=True)
        end_time = time.time()
        processing_time = end_time - start_time
        print(f"MMD file created at {output_mmd_path}")
        print(f"Processing time: {processing_time:.2f} seconds")
        print(f"Command output: {result.stdout}")
        print(f"Command error: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Nougat processing: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return

    if os.path.isdir(output_mmd_path):
        try:
            for root, dirs, files in os.walk(output_mmd_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    s3_key = os.path.relpath(file_path, "/tmp").replace("\\", "/")
                    s3_client.upload_file(file_path, destination_bucket, s3_key)
                    print(f"Uploaded {file_path} to {destination_bucket}/{s3_key}")
        except Exception as e:
            print(f"Error uploading files to S3: {e}")
    else:
        print(f"Expected output directory {output_mmd_path} not found. Skipping upload.")

    if os.path.exists(download_path):
        os.remove(download_path)
        print(f"Local file {download_path} deleted")
    if os.path.exists(output_mmd_path):
        for root, dirs, files in os.walk(output_mmd_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(output_mmd_path)
        print(f"Local directory {output_mmd_path} deleted")

@app.route("", methods=["POST"])
def sns_listener():
    sns_message = json.loads(request.data)

    if sns_message.get("Type") == "SubscriptionConfirmation":
        print("Subscription confirmation received")
        # Confirm the subscription
        subscribe_url = sns_message["SubscribeURL"]
        print(f"Subscribing to URL: {subscribe_url}")
        response = requests.get(subscribe_url)
        print(f"Subscription confirmed: {response.status_code}")
        return jsonify({"message": "Subscription confirmed"}), 200

    elif sns_message.get("Type") == "Notification":
        message = json.loads(sns_message["Message"])
        print("Notification received")
        print(json.dumps(message, indent=2))

        for record in message.get("Records", []):
            # Process each record in a separate thread to avoid blocking
            threading.Thread(target=process_file, args=(record,)).start()

    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run()