import requests
import os
from download_image import download_images
from dotenv import load_dotenv

COLLECTION = "spacecraft"


def fetch_hubble_launch(image_id, images_folder):
  url = f"http://hubblesite.org/api/v3/image/{image_id}"
  response = requests.get(url)
  response.raise_for_status()
  hubble_images = response.json()["image_files"]
  image = hubble_images[-1]
  filename = f'Hubble_{image_id}'
  image_url = "https:" + image['file_url']
  download_images(image_url, filename, os.path.splitext(image["file_url"])[1], images_folder)


def main():
  load_dotenv()
  images_folder = os.environ['IMAGES_FOLDER']
  hubble_url = f"http://hubblesite.org/api/v3/images?page=all&collection_name={COLLECTION}"

  os.makedirs(images_folder, exist_ok=True)

  response = requests.get(hubble_url)
  response.raise_for_status()
  for image in response.json():
    fetch_hubble_launch(image["id"], images_folder)


if __name__ == '__main__':
  main()
