from flask import Flask, request, jsonify
import json
import boto3
import requests
from urllib.parse import unquote_plus

app = Flask(__name__)
s3_client = boto3.client('s3')

@app.route("", methods=["POST"])
def sns_listener():
    sns_message = json.loads(request.data)

    if sns_message.get("Type") == "SubscriptionConfirmation":
        print("Subscription confirmation received")
        # Confirm the subscription
        subscribe_url = sns_message["SubscribeURL"]
        response = requests.get(subscribe_url)
        print("Subscription confirmed:", response.status_code)

    elif sns_message.get("Type") == "Notification":
        message = json.loads(sns_message["Message"])
        print("Notification received")
        print(json.dumps(message, indent=2))

        for record in message.get("Records", []):
            source_bucket = record["s3"]["bucket"]["name"]
            source_key = unquote_plus(record["s3"]["object"]["key"])
            destination_bucket = ""
            destination_key = source_key

            print(f"Checking if file already exists in {destination_bucket}/{destination_key}")
            try:
                s3_client.head_object(Bucket=destination_bucket, Key=destination_key)
                print(f"File already exists: {destination_bucket}/{destination_key}")
                continue  # Skip processing this file
            except s3_client.exceptions.ClientError:
                # The object does not exist, so we can proceed with copying
                print(f"File does not exist: {destination_bucket}/{destination_key}, proceeding with copy")

            print(f"Copying file from {source_bucket}/{source_key} to {destination_bucket}/{destination_key}")

            # Copy the file from source bucket to destination bucket
            copy_source = {'Bucket': source_bucket, 'Key': source_key}
            try:
                s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket, Key=destination_key)
                print(f"File copied to {destination_bucket}/{destination_key}")
            except s3_client.exceptions.NoSuchKey:
                print(f"File not found: {source_key}")

    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)