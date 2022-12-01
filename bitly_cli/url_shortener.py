import requests
import prompt
import os
from dotenv import load_dotenv


def shorten_link(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': long_url}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    long_url = prompt.string('Введите ссылку: ')
    try:
        print('Ваша ссылка: ', shorten_link(long_url, token))
    except requests.exceptions.HTTPError as error:
        print(error)


if __name__ == '__main__':
    main()
