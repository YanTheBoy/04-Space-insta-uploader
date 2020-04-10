import requests
import os


def get_hubble_collections_id(url):
    response = requests.get(url).json()
    for mission in response:
        yield str(mission['id'])


def get_hubble_photo_link(link):
    response = requests.get(link).json()
    return response['image_files'][-1]['file_url']


def fetch_hubble_photo(url, download_folder):
    os.chdir(download_folder)
    filename = '{0}{1}'.format(url.split('/')[-2], url.split('.')[-1])  # image_id from url + pic format
    response = requests.get('https:{}'.format(url), verify=False)

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    image_folder = os.path.join(os.getcwd(), 'images')
    os.makedirs(image_folder, exist_ok=True)

    hubble_spacecraft_data = 'http://hubblesite.org/api/v3/images?page=all&collection_name=spacecraft'
    photos_from_space_mission_by_id = get_hubble_collections_id(hubble_spacecraft_data)
    for mission_id in photos_from_space_mission_by_id:
        hubble_data_url = 'http://hubblesite.org/api/v3/image/{}'.format(mission_id)
        hubble_pic_url = get_hubble_photo_link(hubble_data_url)
        fetch_hubble_photo(hubble_pic_url, image_folder)
