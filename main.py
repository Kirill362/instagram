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

def fetch_spacex_last_launch(url):
  response = requests.get(url)
  response.raise_for_status() 
  spacex_images = response.json()["links"]["flickr_images"]
  for index, image in enumerate(spacex_images):
    download_images(image, f"spacex{index}", detect_extension(image))

def download_images(url, filename, extension):
  response = requests.get(url, verify=False)
  response.raise_for_status() 
  with open(f"./images/{filename}.{extension}", 'wb') as file:
    file.write(response.content)

os.makedirs("./images", exist_ok=True)

filename = 'hubble'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
download_images(url, filename, detect_extension(url))

spacex_url = "https://api.spacexdata.com/v3/launches/99"
fetch_spacex_last_launch(spacex_url)

image_id = 1
fetch_hubble_launch(image_id)