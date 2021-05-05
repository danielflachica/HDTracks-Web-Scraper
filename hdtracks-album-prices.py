'''
Class PriceWebScraper inherits WebScraper
This script reads from a text file which should contain URLs of the HDTracks Albums to be scraped for their prices
Note: The links shouls lead to the HDTrack's API so that the page can be scraped via JSON
'''

from os import path
import csv
from webscraper import WebScraper

URL_FILE = 'links-albums.txt'

class PriceWebScraper(WebScraper):
    def __init__(self, target_url):
        super().__init__(target_url)
        self.price = 0.0
        self.albumID = None
        self.album = None
        self.genre = None

    def scrape(self):
        response = super().load_url()
        self.data = super().to_json(response)
        # for price in self.data['price']['original']:
            # self.prices.append(str(price))
        # self.prices.append(self.data['price']['original'])
        self.price = self.data['price']['original']
        self.albumID = self.data['id']
        self.album = self.data['name']
        self.genre = self.data['genre']

    def export_csv(self, filename:str, data:dict):
        if path.exists(filename):
            super().append_csv(filename, data)
        else:
            super().export_csv(filename, data)
        

if __name__=="__main__":
    prices = []

    if path.exists(URL_FILE):
        with open(URL_FILE) as f:
            lines = f.readlines()
        f.close()
        links = [line.strip() for line in lines]

        with open('hdtracks-album-prices.csv', mode='w') as csv_file:
            csv_headers = ['Album ID', 'Album', 'Genre', 'Price']
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)

            writer.writeheader()
            for target_url in links:
                print('Scraping', target_url)
                price_web_scraper = PriceWebScraper(target_url)
                price_web_scraper.scrape()
                row = {
                    'Album ID': price_web_scraper.albumID,
                    'Album': price_web_scraper.album,
                    'Genre': price_web_scraper.genre,
                    'Price': price_web_scraper.price,
                }
                writer.writerow(row)

    else:
        print('Missing', URL_FILE, 'file')
        exit()
