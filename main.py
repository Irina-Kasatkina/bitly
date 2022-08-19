import os
import argparse
from urllib.parse import urlparse

from dotenv import load_dotenv
import requests


def count_clicks(token: str, bitlink: str) -> int:
    """ Count the number of clicks on the bitlink. """
    bitlink_parts = urlparse(bitlink)
    bitlink = f'{bitlink_parts.netloc}{bitlink_parts.path}'

    bitly_url = (
            'https://api-ssl.bitly.com/v4/bitlinks/'
            f'{bitlink}'
            '/clicks/summary'
    )

    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def create_parser():
    """ Create a command line arguments parser. """
    parser = argparse.ArgumentParser(
            description='Получает с bitly.com короткую ссылку, '
                        'если на вход дан url-адрес. '
                        'Показывает число кликов по bitly ссылке, '
                        'если вход дана bitly ссылка.'
    )
    parser.add_argument(
        'link',
        nargs='?',
        help='Ссылка для укорачивания или bitly ссылка для подсчёта кликов'
    )
    return parser


def is_bitlink(token: str, link: str) -> bool:
    """ Check if the link is a bitlink. """
    link_parts = urlparse(link)
    link = f'{link_parts.netloc}{link_parts.path}'

    bitly_url = (
            'https://api-ssl.bitly.com/v4/bitlinks/'
            f'{link}'
    )

    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(bitly_url, headers=headers)
    return response.ok


def shorten_link(token: str, long_url: str) -> str:
    """ Convert a long link to a short link and return the short link. """
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    json = {'long_url': long_url}

    response = requests.post(bitly_url, headers=headers, json=json)
    response.raise_for_status()
    return response.json()['id']


def main():
    """
    Get a short link from bitly.com if an url is received.
    Show the count of clicks on a bitly link if a bitly link is received.
    """

    parser = create_parser()
    args = parser.parse_args()

    if args.link:
        received_link = args.link.strip()
    else:
        received_link = input('\nВведите ссылку: ').strip()

    load_dotenv()
    token = os.environ['BITLY_TOKEN']

    try:
        bitlink_is_received = is_bitlink(token, received_link)
        if bitlink_is_received:
            clicks_count = count_clicks(token, received_link)
            print(f'Количество перехоодов по ссылке bitly: {clicks_count}')
        else:
            short_link = shorten_link(token, received_link)
            print(f'Короткая ссылка bitly: {short_link}')
    except requests.exceptions.HTTPError as ex:
        print(ex)
        print(f'Введён неправильный url')


if __name__ == '__main__':
    main()
