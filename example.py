import os
import xml.etree.ElementTree as ET

from src import biblionix

bc = biblionix.BiblionixClient(os.environ["BIB_SUBDOMAIN"])
bc.authenticate(os.environ["BIB_CARD_NUMBER"], os.environ["BIB_PASSWORD"])
print(ET.tostring(bc.get_account_info()))
