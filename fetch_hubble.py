import requests
import os
from urllib.parse import urlparse


def detect_extension(url):
  return(url.split(".")[-1])


def fetch_hubble_launch(image_id):
  url = f"http://hubblesite.org/api/v3/image/{image_id}"
  response = requests.get(url)
  response.raise_for_status()
  hubble_images = response.json()["image_files"]
  image = hubble_images[-1]
  filename = f'Hubble_{image_id}'
  image_url = f'https://{urlparse(image["file_url"]).netloc}{urlparse(image["file_url"]).path}'
  download_images(image_url, filename, detect_extension(image["file_url"]))


def download_images(url, filename, extension):
  response = requests.get(url, verify=False)
  response.raise_for_status()
  image_path = f"./images/{filename}.{extension}"
  with open(image_path, 'wb') as file:
    file.write(response.content)


COLLECTION = "spacecraft"

hubble_url = f"http://hubblesite.org/api/v3/images?page=all&collection_name={COLLECTION}"

os.makedirs("./images", exist_ok=True)

response = requests.get(hubble_url)
response.raise_for_status()

for image in eval(response.text):
  fetch_hubble_launch(image["id"])