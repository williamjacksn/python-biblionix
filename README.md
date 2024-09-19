# python-biblionix

Python client library to interface with Biblionix library systems

## Usage

```pycon
>>> import biblionix
>>> # 'library' is the subdomain for your library website
>>> bc = biblionix.BiblionixClient('library')
>>> # username and password you use to sign in to your library website (could be card number instead of username)
>>> bc.authenticate('123456', 'password')
>>> bc.get_account_info()
<Element 'root' at 0x7f5edd54e7a0>
```
