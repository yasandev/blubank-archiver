import requests
from bs4 import BeautifulSoup

blue_bank_url = "https://blubank.com/"


def get_links(url):
    links = []
    website = requests.get(url)
    website_text = website.text
    soup = BeautifulSoup(website_text, "html.parser")

    for link in soup.find_all('a'):
        href = link.get('href')
        links.append(href)

    for link in links:
        print(link)

    print(len(links))


get_links(blue_bank_url)
