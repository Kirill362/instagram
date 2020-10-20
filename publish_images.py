import os
from instabot import Bot
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

LOGIN = ""
PASSWORD = ""

if LOGIN == "":
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

bot = Bot()
bot.login(username=LOGIN, password=PASSWORD)

os.makedirs("./images", exist_ok=True)
os.makedirs("./ready_images", exist_ok=True)
directory = './images/'
images = os.listdir(directory)

for filename in images:
    image_path = f"./images/{filename}"
    image = Image.open(image_path)
    if image.width > image.height:
        if image.height > 1080:
            image.thumbnail((1080, 1080))
        else:
            image.thumbnail((1080, image.height))
    else:
        if image.width > 1080:
            image.thumbnail((1080, 1080))
        else:
            image.thumbnail((image.width, 1080))
    rgb_im = image.convert("RGB")
    image_name = filename.split(".")[0]
    rgb_im.save(f"./ready_images/{image_name}.jpg", format="JPEG")
    bot.upload_photo(f"./ready_images/{image_name}.jpg", caption="Hello")