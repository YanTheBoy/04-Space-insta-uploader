import requests
import os


def get_spacex_last_launch_pictures_links(url):
    response = requests.get(url).json()
    return response['links']['flickr_images']


def fetch_spacex_last_launch_photo(url, download_folder):
    os.chdir(download_folder)
    # filename = url.split('/')[-1]
    filename = url.split('/')[-1].split('.')[0]
    response = requests.get(url)

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    image_folder = os.path.join(os.getcwd(), 'images')
    os.makedirs(image_folder, exist_ok=True)

    spacex_last_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    list_spacex_pics = get_spacex_last_launch_pictures_links(spacex_last_launch_url)
    for link in list_spacex_pics:
        fetch_spacex_last_launch_photo(link, image_folder)
