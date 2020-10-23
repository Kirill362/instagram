import requests
import os
from urllib.parse import urlparse
from download_image import download_images
from dotenv import load_dotenv


def main():
  load_dotenv()
  IMAGES_FOLDER = os.environ['IMAGES_FOLDER']
  COLLECTION = "spacecraft"

  hubble_url = f"http://hubblesite.org/api/v3/images?page=all&collection_name={COLLECTION}"

  os.makedirs(IMAGES_FOLDER, exist_ok=True)

  response = requests.get(hubble_url)
  response.raise_for_status()
  for image in response.json():
    fetch_hubble_launch(image["id"])


def fetch_hubble_launch(image_id):
  url = f"http://hubblesite.org/api/v3/image/{image_id}"
  response = requests.get(url)
  response.raise_for_status()
  hubble_images = response.json()["image_files"]
  image = hubble_images[-1]
  filename = f'Hubble_{image_id}'
  image_url = f'https://{urlparse(image["file_url"]).netloc}{urlparse(image["file_url"]).path}'
  download_images(image_url, filename, os.path.splitext(image["file_url"])[1])


if __name__ == '__main__':
  main()
