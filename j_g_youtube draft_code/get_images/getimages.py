#practice py script for scraping images
import requests
from bs4 import BeautifulSoup as bs
import os

#website with images
url = 'https://designyoutrust.com/2018/06/magnificent-nsfw-modelling-photo-artworks-by-the-russian-photographer-nikolas-verano/'

#dowmload page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#locate all elements with image tag
images_tags = soup.findAll('img')

# create dir for model images
if not os.path.exists('images'):
    os.makedirs('images')

#move to new directorires
os.chdir('images')

#image file name variable
x = 0

#writing images
for image in images_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('image-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
