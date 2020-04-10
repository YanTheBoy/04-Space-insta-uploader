from dotenv import load_dotenv
from instabot import Bot
from PIL import UnidentifiedImageError
from PIL import Image
import os


def thumbnail_photo(pic_name):
    image = Image.open(pic_name)
    image.thumbnail((1080, 1080))
    return image


def save_photo_in_jpg(picture, pic_name):
    picture = picture.convert('RGB')  # miss OSError with RGBA
    picture.save('{}.jpg'.format(pic_name), format='JPEG')


if __name__ == '__main__':
    os.chdir(os.path.join(os.getcwd(), 'images'))
    photo_list = os.listdir(os.getcwd())
    for photo in photo_list:
        try:
            resized_pic = thumbnail_photo(photo)
            save_photo_in_jpg(resized_pic, photo)
        except UnidentifiedImageError:
            pass
'''
  load_dotenv()
    instagram_login = os.getenv('INSTA_LOGIN')
    instagram_password = os.getenv('INSTA_PASS')

    bot = Bot()
    bot.login(
        username=instagram_login,
        password=instagram_password,
        ask_for_code=True
    )

    for photo in photo_list:
        if photo.endswith('.jpg'):
            bot.upload_photo(photo, caption='one more amazing space pic!')
'''

