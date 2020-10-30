import os
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
IMAGES_FOLDER = os.environ['IMAGES_FOLDER']
LOGIN = os.environ['LOGIN']
PASSWORD = os.environ['PASSWORD']


def main():
    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)

    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    os.makedirs("./ready_images", exist_ok=True)
    images = os.listdir(IMAGES_FOLDER)

    for filename in images:
        image_path = f"{IMAGES_FOLDER}/{filename}"
        image = Image.open(image_path)
        image.thumbnail((1080, 1080))
        image_name = filename.split(".")[0]
        image.save(f"./ready_images/{image_name}.jpg", format="JPEG")
        try:
            bot.upload_photo(f"./ready_images/{image_name}.jpg", caption="Hello")
        except:
            continue


if __name__ == '__main__':
    main()
