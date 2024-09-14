import requests
from bs4 import BeautifulSoup as bs
from loguru import logger


class Trail:
    def __init__(self, name: str, length: int, rating):
        self.name = name
        self.length = length
        self.rating = rating

    def __str__(self):
        return f"{self.name} is {self.length} miles long and has a {self.rating} star rating"


def parse_trails(url: str) -> list[Trail]:
    """
    Given a url from AllTrails, return a list of Trails
    """

    result = requests.get(url, headers={'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
    doc = bs(result.text, "html.parser")
    print(doc)
    # trails = doc.find_all('div')
    # for trail in trails:
    #     try:
    #         print(trail.get('href'))
    #     except AttributeError:
    #         print('No link')

