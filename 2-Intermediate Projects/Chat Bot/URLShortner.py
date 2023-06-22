from typing import Final
import requests

api_key: Final[str]= '' ## Enter api_key
page_url: Final[str] = 'https://cutt.ly/api/api.php'

def shorten_link(full_link: str):
    payload: dict = {'key': api_key, 'short': full_link}
    request = requests.get(page_url, params = payload)
    data: dict = requests.json()

    if url_data := data.get('url'):
        if url_data['status'] == 7:
            short_link: str = url_data['shortLink']
            print(f'Link: {short_link}')
        else:
            print('Error status', url_data['status'])

def main():
    input_link: str = input('Enter a link ')
    shorten_link(input_link)

if __name__ == '__main__':
    main()