#Remember to add cookie block or you can have some captchas from reddit :) 

from bs4 import BeautifulSoup
import requests
import json

url = input('Input Redit url below:')

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': #add your cookie,
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Referer': 'https://www.reddit.com/',
    'Origin': 'https://www.reddit.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'origin': 'https://www.reddit.com',
    'referer': 'https://www.reddit.com/',
    'content-type': 'text/PLAIN',
    'x-sh-microapp-route': 'monolith',
    'Content-Type': 'text/plain;charset=UTF-8'
  }

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(response.text)
#heading
try:
    getheading = soup.find('h1', attrs={'slot':'title'})
    heading = getheading.text.strip()
except:
    heading = 'Null'

#content
contentsoup1 = soup.find('div', attrs={'id':'t3_1boenvi-post-rtjson-content'})
contentsoup3 = contentsoup1.find('p')
content = contentsoup3.text.strip()
print(content)


# PRINTING
print('Heading -> ' + heading)
print('Content -> '+ content)
