import requests
from dotenv import load_dotenv
import os


def download_images(url, filename, extension):
  load_dotenv()
  IMAGES_FOLDER = os.environ['IMAGES_FOLDER']
  response = requests.get(url, verify=False)
  response.raise_for_status()
  image_path = f"{IMAGES_FOLDER}/{filename}{extension}"
  with open(image_path, 'wb') as file:
    file.write(response.content)
