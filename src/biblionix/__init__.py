__version__ = "2025.1"

import dataclasses
import datetime
import httpx
import xml.etree.ElementTree


@dataclasses.dataclass
class LibraryLoan:
    item_id: str
    title: str
    subtitle: str
    medium: str
    due: datetime.date
    renewable: bool


class BiblionixClient:
    session_key: str

    def __init__(self, library_subdomain: str):
        self.library_subdomain = library_subdomain
        self.httpx_client = httpx.Client()

    def authenticate(self, username: str, password: str):
        url = f"https://{self.library_subdomain}.biblionix.com/catalog/ajax_backend/login.xml.pl"
        data = {
            "username": username,
            "password": password,
        }
        login = self.httpx_client.post(url=url, data=data)
        login.raise_for_status()
        login_et = xml.etree.ElementTree.XML(login.text)
        self.session_key = login_et.get("session")

    def get_account_info(self) -> xml.etree.ElementTree:
        account_url = f"https://{self.library_subdomain}.biblionix.com/catalog/ajax_backend/account.xml.pl"
        account_data = {"session": self.session_key}
        account = self.httpx_client.post(url=account_url, data=account_data)
        account_et = xml.etree.ElementTree.XML(account.text)
        return account_et

    @property
    def loans(self) -> list[LibraryLoan]:
        result = []
        account_info = self.get_account_info()
        for item in account_info.findall("item"):
            result.append(
                LibraryLoan(
                    item_id=item.get("id"),
                    title=item.get("title").replace("\xad", ""),
                    subtitle="",
                    medium=item.get("medium").replace("\xad", ""),
                    due=datetime.date.fromisoformat(item.get("due_raw")),
                    renewable=item.get("renewable") == "1",
                )
            )
        return result
