import requests
import argparse
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(long_url, token):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    header = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': long_url}
    response = requests.post(bitly_url, headers=header, json=payload)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(bitlink, token):
    parsed_url = urlparse(bitlink)
    basic_url = f'{parsed_url.netloc}{parsed_url.path}'
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{basic_url}/clicks/summary'  # noqa: E501
    header = {'Authorization': f'Bearer {token}'}
    payload = {
        'units': -1,
        'unit': 'day'
    }
    response = requests.get(bitly_url, headers=header, params=payload)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(url, token):
    parsed_url = urlparse(url)
    basic_url = f'{parsed_url.netloc}{parsed_url.path}'
    header = {'Authorization': f'Bearer {token}'}
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{basic_url}'
    response = requests.get(bitly_url, headers=header)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description='The script creates short link via Bitly API and counts clicks on it')  # noqa: E501
    parser.add_argument('url', help='Enter short or long URL')
    args = parser.parse_args()
    user_url = args.url

    if is_bitlink(user_url, token):
        try:
            print('Total clicks: ', count_clicks(user_url, token))
        except requests.exceptions.HTTPError as error:
            print(error)
    else:
        try:
            print('Bitlink: ', shorten_link(user_url, token))
        except requests.exceptions.HTTPError as error:
            print(error)


if __name__ == '__main__':
    main()
