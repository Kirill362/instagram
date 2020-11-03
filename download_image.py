import requests


def download_images(url, filename, extension, images_folder):
  response = requests.get(url, verify=False)
  response.raise_for_status()
  image_path = f"{images_folder}/{filename}{extension}"
  with open(image_path, 'wb') as file:
    file.write(response.content)
