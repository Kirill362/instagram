import requests
import os
from download_image import download_images
from dotenv import load_dotenv

IMAGES_ID = 99


def main():
  load_dotenv()
  images_folder = os.environ['IMAGES_FOLDER']

  spacex_url = f"https://api.spacexdata.com/v3/launches/{IMAGES_ID}"

  os.makedirs(images_folder, exist_ok=True)

  fetch_spacex_last_launch(spacex_url, images_folder)


def fetch_spacex_last_launch(url, images_folder):
  response = requests.get(url)
  response.raise_for_status()
  spacex_images = response.json()["links"]["flickr_images"]
  for index, image in enumerate(spacex_images):
    download_images(image, f"spacex{index}", os.path.splitext(image)[1], images_folder)


if __name__ == '__main__':
  main()
