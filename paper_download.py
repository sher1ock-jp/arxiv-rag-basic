import requests
import os

save_path = './paper_input_storage'

def download_paper(pdf_url, paper_title):

    split_title = paper_title.split(" ")
    file_title = "_".join(split_title[:3])
    file_name = f"{file_title}.pdf"

    try:
        if not pdf_url.startswith('http'):
            raise ValueError("Invalid URL")
        
        response = requests.get(pdf_url)
        response.raise_for_status()

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        pdf_path = os.path.join(save_path, file_name)
        
        with open(pdf_path, 'wb') as file:
            file.write(response.content)
        print("PDF downloaded successfully")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")