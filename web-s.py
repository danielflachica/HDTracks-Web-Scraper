'''
This is the first web scraping script I wrote, taken from some website tutorial
IMPORTANT NOTE: The code here only works if the web page is rendered SERVER-SIDE (not client-side)
To check this, go to your target web page, right click and view the page source. If It doesn't look weird or like it's missing
any elements, you're good to go. Otherwise, it could mean that the HTML elements are rendered client-side (on your browser), 
so there's no way that this web scraper will find the elements using the page source (cuz they don't exist yet)

For a workaround to this issue, see the WebScraper class in "webscraper.py" which scrapes from JSON data instead of page source
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set up web driver
driver = webdriver.Chrome(ChromeDriverManager().install())

products, prices, ratings = [], [], []

URL = 'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2'
driver.get(URL)

# Load web page's HTML structure into a variable
content = driver.page_source

# Initialize beatiful soup
soup = BeautifulSoup(content, features="html.parser")

# Begin web scraping
for a in soup.findAll('a', href=True, attrs={'class':'_1fQZEK'}):
    # Scrape data given the element's classes (you need to know these beforehand by checking the page source yourself)
    product = a.find('div', attrs={'class':'_4rR01T'}).text.strip()
    price = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'}).text.strip()
    rating = a.find('div', attrs={'class':'_3LWZlK'}).text.strip()

    products.append(product)
    prices.append(price)
    ratings.append(rating)

# print(products)
# print(prices)
# print(ratings)

# Output to csv
df = pd.DataFrame({
    'Product Name': products,
    'Price': prices,
    'Rating': ratings,
})
print(df)
df.to_csv('products.csv', index=False, encoding='utf-8')

print('DONE WEB SCRAPING')