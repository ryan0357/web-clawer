from bs4 import BeautifulSoup as bsp
from PIL import Image
import requests as rqs
import os

def main():
    keyword = 'hololive'
    response = rqs.get('https://imgur.com/search?q={}'.format(keyword))
    html = bsp(response.text, 'html.parser')
    element = html.find_all(name = 'div', attrs = {'class', 'cards'})[0]
    picture = element.find_all(name = 'img')
    
    picture_urls = []
    for i in picture:
        picture_urls.append(i.get('src')[14:])
    for i in picture_urls:
        res_pic = rqs.get(f'http://imgur.com/{i}', stream = True, timeout = 5)
        image = Image.open(res_pic.raw)
        image.show()
        os.system('pause')

if __name__ == '__main__':
    main()