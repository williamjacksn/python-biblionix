__version__ = '2023.0'

import dataclasses
import urllib.parse
import urllib.request
import xml.etree.ElementTree


@dataclasses.dataclass
class LibraryAccount:
    library: str
    username: str
    password: str

    _session_key: str = dataclasses.field(init=False, repr=False, default=None)

    def sign_in(self):
        url = f'https://{self.library}.biblionix.com/catalog/ajax_backend/login.xml.pl'
        data = {
            'password': self.password,
            'username': self.username,
        }
        response = urllib.request.urlopen(url, urllib.parse.urlencode(data).encode())
        page = response.read().decode()
        et = xml.etree.ElementTree.XML(page)
        self._session_key = et.get('session')
