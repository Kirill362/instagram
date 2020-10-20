import requests
import os


def detect_extension(url):
  return(url.split(".")[-1])


def fetch_spacex_last_launch(url):
  response = requests.get(url)
  response.raise_for_status()
  spacex_images = response.json()["links"]["flickr_images"]
  for index, image in enumerate(spacex_images):
    download_images(image, f"spacex{index}", detect_extension(image))


def download_images(url, filename, extension):
  response = requests.get(url, verify=False)
  response.raise_for_status()
  image_path = f"./images/{filename}.{extension}"
  with open(image_path, 'wb') as file:
    file.write(response.content)


IMAGES_ID = 99
spacex_url = f"https://api.spacexdata.com/v3/launches/{IMAGES_ID}"

os.makedirs("./images", exist_ok=True)

fetch_spacex_last_launch(spacex_url)