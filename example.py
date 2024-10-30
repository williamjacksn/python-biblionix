import os
import xml.etree.ElementTree

from src import biblionix

bc = biblionix.BiblionixClient(os.getenv('BIB_SUBDOMAIN'))
bc.authenticate(os.getenv('BIB_CARD_NUMBER'), os.getenv('BIB_PASSWORD'))
print(xml.etree.ElementTree.tostring(bc.get_account_info()))
