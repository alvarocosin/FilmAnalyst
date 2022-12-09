import requests
from bs4 import BeautifulSoup

q = 'Lawrence of Arabia'
query = q.replace(' ', '+')
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
url = 'https://www.filmaffinity.com/es/search.php?stext=' + query
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

results = list()
search = soup.find_all('div', class_='mc-title')
for film in search:
    for element in film.find_all('a'):
        link = element['href']
        results.append(link)

url = results[0]
print(url)
# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.content, 'lxml')

# rating = soup.find('div', id='movie-rat-avg').text
# n_ratings = soup.find('span', itemprop='ratingCount').text
# country = soup.find('span', id='country-img')
# for cname in country:
#     country_name = cname['alt']
# runtime = soup.find('dd', itemprop='duration').text