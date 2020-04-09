# Space Instagram
The script was written for downloading Hubble and SpaceX photos, then resize photo for instagram requirements and upload
photos to your instagram account

# How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
$ pip install -r requirements.txt
```

Create .env file in your repository and put there your instagram login and password.
```text
INSTA_LOGIN=your_login
INSTA_PASS=your_instagram_password
```
Download photos from SpaceX API or Hubble API. Scripts will download photos and put them in new Image directory.
```bash
$ python3 fetch_hubble.py
$ python3 fetch_spacex.py
```
Run insta-uploader.py for cropping images and uploading in instagram
```bash
$ python3 insta-uploader.py
2020-04-09 23:46:11,532 - INFO - Instabot version: 0.117.0 Started
2020-04-09 23:46:11,533 - INFO - Recovery from /home/elijah/Documents/projects/04-insta-uploader/...
- user-agent=Instagram 117.0.0.28.123 Android (28/9.0; 420dpi; 1080x1920; OnePlus; ONEPLUS A3003...
- phone_id=e8366abe-878c-45a7-affb-cffa27a5ad1a
- uuid=9f5c886e-ef87-47d7-acbc-4fd20e02ea75
- client_session_id=00e04029-7210-4e46-84fc-e007123afb78
- device_id=android-9718f29a517f0ee4
2020-04-09 23:46:11,533 - INFO - LOGIN FLOW! Just logged-in: False
2020-04-09 23:46:13,039 - INFO - Logged-in successfully as 'cosmo_vibes2020'!
FOUND: w:720 h:1080 r:0.6666666666666666
```


# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)