'''
This is the Parent Class for all of the Web Scrapers I've implemented 
Note: This is for scraping JSON objects, traditional web scraping methods are available in "web-s.py"
Note: The scrape() method was left blank since each child has its own implementation of scraping
Note: It's not perfect yet, but I've also defined methods for exporting scraped data to json and csv
'''

import json
import pandas as pd
import time
import urllib.request
import csv

class WebScraper:
    def __init__(self, target_url):
        self.target_url = target_url
        self.data = {}
    
    def scrape(self):
        pass

    def load_url(self):
        response = urllib.request.urlopen(self.target_url)
        return response

    def to_json(self, response):
        json_response = json.load(response)
        return json_response

    def export_csv(self, filename='hdtracks.csv', data=None):
        t0 = time.time()
        df = pd.DataFrame.from_dict(data if data is not None else self.data)
        df.to_csv(filename, header=True, index=False, encoding='utf-8')
        print('Exported', filename, 'in', time.time()-t0, 'seconds')

    def export_json(self, filename='hdtracks.json', data=None):
        t0 = time.time()
        with open(filename, 'w') as outfile:
            json.dump(data if data is not None else self.data, outfile, sort_keys=True, indent=4)
        print('Exported', filename, 'in', time.time()-t0, 'seconds')

    def append_csv(self, filename='hdtracks.csv', data=None):
        t0 = time.time()
        # df = pd.DataFrame.from_dict(data if data is not None else self.data)
        # df.to_csv(filename, mode='a', header=False, index=False, encoding='utf-8')
        with open(filename, 'a') as csvfile:
            # headers = ['Field{}'.format(i) for i in range(1,len(data if data is not None else self.data))]
            headers = ['id', 'name', 'mainArtist', 'cover', 'label', 'genre', 'release', 'duration', 'tracksCount', 'views', 'rate', 'resolution', 'quality']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            # writer.writeheader()
            for d in data if data is not None else self.data:
                writer.writerow(d)
        print('Appended to', filename, 'in', time.time()-t0, 'seconds')

    def append_json(self, filename='hdtracks.json', data=None):
        t0 = time.time()
        with open(filename, 'a') as outfile:
            json.dump(data if data is not None else self.data, outfile, sort_keys=True, indent=4)
        print('Appended to', filename, 'in', time.time()-t0, 'seconds')

    def clean_json_structure(self, filename):
        with open(filename, 'r') as raw_json:
            structured_json = raw_json.read().replace('}{', '},{').replace('\n', '')
            structured_json = '[' + structured_json + ']'
            with open(filename, 'w') as outfile:
                json.dump(structured_json, outfile, sort_keys=True, indent=4)
        print('Cleaned up JSON!')

    def get_target_url(self):
        return self.target_url

    def get_data(self):
        return self.data

    def set_target_url(self, target_url):
        self.target_url = target_url

    def set_data(self, data):
        self.data = data
