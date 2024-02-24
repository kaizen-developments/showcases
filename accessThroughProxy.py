import requests

import requests
from bs4 import BeautifulSoup

from typing import Dict, List

import logging

logging.basicConfig(level=logging.INFO)

url = "https://www.invaluable.com/search?query=Search&keyword=Search"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept": "application/json",  # Tell the server what content types you accept
}
#response = requests.get(url, headers=headers)
css = ".hit-wrapper"
#print(response.text)

URL=str
Attribute = str
CssSelector = str
DataModel = Dict[Attribute, CssSelector]

def getTableData(url: URL, tablePattern: CssSelector, tableItemPattern: CssSelector, dataModel: DataModel) -> List[Dict[Attribute, str]]:
    logging.info(f"Getting data from {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.select_one(tablePattern)
    logging.info(f"Identified table: {table}")
    items = table.select(tableItemPattern)
    logging.info(f"Identified items: {items}")

    data = []
    for item in items:
        item_data = {}
        for attribute, selector in dataModel.items():
            element = item.select_one(selector)
            item_data[attribute] = element.text if element else None
        data.append(item_data)
        logging.info(f"Added item: {item_data}")

    return data

getTableData("https://www.invaluable.com/search?query=Search&keyword=Search", "div", "div", {"name": "a.lot-title.text"})