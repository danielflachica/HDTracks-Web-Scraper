import csv
from os import path
import time


URL_TEMPLATE = 'https://hdtracks.azurewebsites.net/api/v1/album/'
URL_FILE = 'links-albums.txt'
CSV_FILE = 'hdtracks-albums.csv'
# CSV_FILE = 'test.csv'


def build_url(id):
    return URL_TEMPLATE + id + '?token=123456789'


if __name__=="__main__":
    if path.exists(CSV_FILE):
        t0 = time.time()
        with open(CSV_FILE, 'r') as infile:
            reader = csv.reader(infile)
            outfile = open(URL_FILE, 'w')
            next(reader, None)  # skip header row

            for row in reader:
                album_id, album_name = row[0], row[1]
                print('Processing', album_name, 'with ID', album_id)
                url = build_url(album_id)
                outfile.write(url + '\n')

            outfile.close()
        print('Created', URL_FILE, 'in', time.time()-t0, 'seconds')
    else:
        print(CSV_FILE, 'not found. Exiting app')
        exit()