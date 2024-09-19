__version__ = '2024.0'

import httpx
import xml.etree.ElementTree


class BiblionixClient:
    session_key: str

    def __init__(self, library_subdomain: str):
        self.library_subdomain = library_subdomain
        self.httpx_client = httpx.Client()

    def authenticate(self, username: str, password: str):
        url = f'https://{self.library_subdomain}.biblionix.com/catalog/ajax_backend/login.xml.pl'
        data = {
            'username': username,
            'password': password,
        }
        login = self.httpx_client.post(url=url, data=data)
        login.raise_for_status()
        login_et = xml.etree.ElementTree.XML(login.text)
        self.session_key = login_et.get('session')

    def get_account_info(self) -> xml.etree.ElementTree:
        account_url = f'https://{self.library_subdomain}.biblionix.com/catalog/ajax_backend/account.xml.pl'
        account_data = {'session': self.session_key}
        account = self.httpx_client.post(url=account_url, data=account_data)
        account_et = xml.etree.ElementTree.XML(account.text)
        return account_et
