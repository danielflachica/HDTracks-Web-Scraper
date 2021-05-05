'''
This script is just a duplicate checker I wrote to make things easier when I was gathering links for scraping
Note: In hindisght, I should've noticed the pattern in the links earlier on. I could have programmatically generated them
instead of using this to check if I copy-pasted duplicate links -_-
'''

from os import path

filename =  input('Enter filename: ')

if path.exists(filename):
    with open(filename, 'r') as outfile:
        lines = outfile.readlines()
    links = [line.strip() for line in lines]
else:
    links = []

while True:
    try:
        link = input('Enter link: ')
        if link not in links:
            links.append(link)
            with open(filename, 'a') as outfile:
                outfile.write(link+'\n')
        else:
            print('Duplicate link detected!')
            
    except EOFError:
        print('Exiting app')
        exit()
