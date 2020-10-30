import requests
import os
from download_image import download_images
from dotenv import load_dotenv

load_dotenv()
IMAGES_FOLDER = os.environ['IMAGES_FOLDER']
IMAGES_ID = 99


def main():
  spacex_url = f"https://api.spacexdata.com/v3/launches/{IMAGES_ID}"

  os.makedirs(IMAGES_FOLDER, exist_ok=True)

  fetch_spacex_last_launch(spacex_url)


def fetch_spacex_last_launch(url):
  response = requests.get(url)
  response.raise_for_status()
  spacex_images = response.json()["links"]["flickr_images"]
  for index, image in enumerate(spacex_images):
    download_images(image, f"spacex{index}", os.path.splitext(image)[1])


if __name__ == '__main__':
  main()
