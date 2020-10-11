from bs4 import BeautifulSoup
import requests

'''scraping kênh 14'''

search = input('Enter your website:')  # take in search request
# params = {'q': search}  # assign q
r = requests.get(f'https://kenh14.vn/{search}.html')  # access web
soup = BeautifulSoup(r.text, 'html.parser')  # parse through the source
result = soup.find('li', {'class': 'knswli need-get-value-facebook clearfix'})

for result in soup.find_all('li', {'class': 'knswli need-get-value-facebook clearfix'}):

    headline = result.h3.a.text
    print(headline)

    intro = result.find('span', {'class': 'knswli-sapo'})
    if intro is None:
        print('This article has no intro')
    else:
        print(intro.text)

    link = result.find('a', {'class': 'kscliw-ava'})['href']
    print('https://kenh14.vn' + link + '\n')

