from dotenv import load_dotenv
from instabot import Bot
from PIL import Image
import os


def thumbnail_photo(pic_name):
    image = Image.open(pic_name)
    width, height = image.size
    if width > height:
        image.thumbnail((1080, 1080))  # 90:47 (max width 1080 px) if horizontal
    elif image.size[0] == image.size[1]:
        image.thumbnnail((1080, 1080))  # 1:1 (1080x1080 px) if square
    else:
        image.thumbnail((1080, 1080))  # 4:5 (max height 1080 px) if vertical
    return image


def save_photo_in_jpg(photo, pic_name):
    photo = photo.convert('RGB')  # miss OSError with RGBA
    photo.save(pic_name + '.jpg', format='JPEG')


if __name__ == '__main__':
    img_file_path = os.getcwd() + '/images'

    os.chdir(os.getcwd() + '/images')
    photo_list = os.listdir(os.getcwd())
    for photo_name in photo_list:
        try:
            resized_pic = thumbnail_photo(photo_name)
            save_photo_in_jpg(resized_pic, photo_name)
        except:    # catch non-image files
            pass

    load_dotenv()
    login = os.getenv('INSTA_LOGIN')
    passw = os.getenv('INSTA_PASS')

    bot = Bot()
    bot.login(username=login, password=passw, ask_for_code=True)

    photo_list = os.listdir(os.getcwd())
    for photo_name in photo_list:
        if photo_name.endswith('.jpg'):
            bot.upload_photo(photo_name, caption='one more amazing space pic!')
