# Lee una lista de películas desde un .txt y los escribe en una hoja excel
import pandas as pd
from movie import Movie
import requests
from bs4 import BeautifulSoup

def make_list():
    print('Starting program...\nIt might take a while')
    with open('pelis2021.txt') as f:
        lines = f.readlines()
    f.close()

    movies = list()

    for line in lines:
        line = line.strip()
        firstbreak = line.find('(')
        title = line[2:firstbreak - 1]
        year = line[firstbreak + 1:firstbreak + 5]
        secondbreak = line.find('.')
        director = line[secondbreak + 2:]
        movie = Movie(title=title, year=year, director=director)
        movies.append(movie)
    return movies

def get_movies_data(movie_list):
    titles = list()
    years = list()
    directors = list()
    ratings = list()
    number_ratings = list()
    for movie in movie_list:
        q = movie.title + " " + movie.year
        query = q.replace(' ', '+')
        headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
        url = 'https://www.imdb.com/find?q=' + query
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')

        results = list()
        for search in soup.find_all('a', class_='ipc-metadata-list-summary-item__t'):
            link = search['href']
            results.append(link)
        movie_id = results[0]

        url = 'https://www.imdb.com' + movie_id
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')

        rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').text
        n_ratings = soup.find('div', class_='sc-7ab21ed2-3 dPVcnq').text
        ratings.append(rating)
        number_ratings.append(n_ratings)
    for movie in movie_list:
        titles.append(movie.title)
        years.append(movie.year)
        directors.append(movie.director)
    length = len(movie_list)
    df = pd.DataFrame({'Title': titles, 'Year': years, 'Director': directors, 'Rating on iMDB': ratings, 'Number of ratings': number_ratings}, index=list(range(1,length+1)))
    df.to_csv('Pelis2021.csv', index = False)
    print('Done')

def main():
    movies = make_list()
    get_movies_data(movies)

if __name__ == '__main__':
    main()