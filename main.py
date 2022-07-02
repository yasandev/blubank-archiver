import os
import urllib
import requests
from bs4 import BeautifulSoup

BLU_BANK_URL = "https://blubank.sb24.ir/"


def get_links(url):
    print("Loading", url)

    links = []
    website = requests.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}, timeout=15)
    website_text = website.text
    soup = BeautifulSoup(website_text, "html.parser")

    for link in soup.find_all('a', {"class": "footer__btn"}):
        href = str(link.get('href'))
        if ".apk" in href:
            links.append(href)

    print("Found", len(links), "apk links")

    for link in links:
        print(link)

    print("Starting to download apk files")

    for link in links:
        print("Starting to download", link)
        # Split on the rightmost / and take everything on the right side of that
        name = link.rsplit('/', 1)[-1]
        filename = os.path.join("./downloads", name)

        # Download the file if it does not exist
        if not os.path.isfile(filename):
            print("Starting download")
            urllib.request.urlretrieve(link, filename)
        else:
            print("File already downloaded")


get_links(BLU_BANK_URL)
