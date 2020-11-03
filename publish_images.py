import os
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv


def main():
    load_dotenv()
    images_folder = os.environ['IMAGES_FOLDER']
    login = os.environ['LOGIN']
    password = os.environ['PASSWORD']

    bot = Bot()
    bot.login(username=login, password=password)

    os.makedirs(images_folder, exist_ok=True)
    os.makedirs("./ready_images", exist_ok=True)
    images = os.listdir(images_folder)

    for filename in images:
        image_path = f"{images_folder}/{filename}"
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
