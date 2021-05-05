'''
Class GenreWebScraper inherits WebScraper
Given a link to HDTrack's API for Genres (in JSON), this script gathers the unique genres available on the website
Note: If the script detects that file "links-generes.txt" exists, it will append the respective links to the csv outfile
'''

import time
import pandas as pd
from os import path
from webscraper import WebScraper

TARGET_URL = 'https://hdtracks.azurewebsites.net/api/v1/genres/search?sort=name&perPage=106&page=1&token=123456789'

class GenreWebScraper(WebScraper):
    def __init__(self, target_url):
        super().__init__(target_url)
        self.genres = []
        self.song_counts = []

    def scrape(self):
        response = super().load_url()
        self.data = super().to_json(response)
        for genre in self.data['genres']:
            self.genres.append(genre)

    def export_json(self, filename='hdtracks-genres.json'):
        super().export_json(filename)

    def export_csv(self, filename='hdtracks-genres.csv'):
        t0 = time.time()
        self.song_counts = [0] * len(self.genres)   # fill with placeholders
        df = pd.DataFrame({
            'Genre': self.genres,
            'Song Count': self.song_counts,
            'Links': self.data['links']
        })
        df.to_csv(filename, index=False, encoding='utf-8')
        print('Exported', filename, 'in', time.time()-t0, 'seconds')

    def append_links_to_genres(self):
        if path.exists('links-genres.txt'):
            with open('links-genres.txt') as f:
                lines = f.readlines()
            f.close()
            links = [line.strip() for line in lines]
            self.data['links'] = links
    

if __name__=="__main__":
    genre_web_scraper = GenreWebScraper(TARGET_URL)
    genre_web_scraper.scrape()

    genre_web_scraper.append_links_to_genres()

    genre_web_scraper.export_json()
    genre_web_scraper.export_csv()