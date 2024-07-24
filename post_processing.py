import requests
import os

save_path = './pdf_storage'

def download_pdf(pdf_url):
    try:
        if not pdf_url.startswith('http'):
            raise ValueError("Invalid URL")
        
        response = requests.get(pdf_url)
        response.raise_for_status()

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        pdf_path = os.path.join(save_path, 'downloaded_paper.pdf')
        
        with open(pdf_path, 'wb') as file:
            file.write(response.content)
        print("PDF downloaded successfully")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")