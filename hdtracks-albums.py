'''
Class AlbumWebScraper inherits WebScraper
This script reads from a text file which should contain URLs of the HDTracks Genres to be scraped for their info
Info to be scraped includes Album Name, Album ID, Genre, Song Count, etc.
Note: The links shouls lead to the HDTrack's API so that the page can be scraped via JSON
'''

from os import path
from webscraper import WebScraper


class AlbumWebScraper(WebScraper):
    def __init__(self, target_url):
        super().__init__(target_url)
        
    def scrape(self):
        response = super().load_url()
        self.data = super().to_json(response)

    def export_csv(self, filename='hdtracks-albums.csv'):
        album_data = self.strip_album_data(self.data['albums'])
        if path.exists(filename):
            super().append_csv(filename, album_data)
        else:
            super().export_csv(filename, album_data)

    def export_json(self, filename='hdtracks-albums.json'):
        if path.exists(filename):
            super().append_json(filename)
        else:
            super().export_json(filename)

    def strip_album_data(self, data:dict):
        stripped_data = data
        for album in stripped_data:
            del album['@search.score']
            del album['artists']
            del album['bundled']
            del album['cLine']
            del album['pLine']
            del album['upc']
            del album['pdf']
            del album['originalRelease']
            del album['preOrder']
        return stripped_data


if __name__=="__main__":
    if path.exists('links-genres.txt'):
        all_album_data = []

        with open('links-genres.txt') as f:
            lines = f.readlines()
        f.close()
        links = [line.strip() for line in lines]
        
        for target_url in links:
            album_web_scraper = AlbumWebScraper(target_url)
            album_web_scraper.scrape()

            # album_web_scraper.export_json('hdtracks-albums.json')
            album_web_scraper.export_csv()

        # album_web_scraper.clean_json_structure('hdtracks-albums.json')
    else:
        print('Missing links-genres.txt file')
        exit()
    