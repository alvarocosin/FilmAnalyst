# Lee una lista de películas desde un .txt y los escribe en una hoja excel
import pandas as pd
from movie import Movie
import requests
from bs4 import BeautifulSoup
import colorama

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

def progress_bar(progress, total, color = colorama.Fore.YELLOW):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(color + f"\r|{bar}| {percent:.2f}%", end="\r") 
    if(progress == total):
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")  


def get_movies_data(movie_list):
    titles = list()
    years = list()
    directors = list()
    runtimes = list()
    countries = list()
    ratings = list()
    number_ratings = list()
    
    cont = 0
    total = len(movie_list)
    progress_bar(cont, total)
    for movie in movie_list:
        q = movie.title
        query = q.replace(' ', '+')
        headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
        url = 'https://www.filmaffinity.com/es/search.php?stext=' + query
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'lxml')
        search = soup.find_all('div', class_='mc-title')
        if(len(search) > 0):
            results = list()
            search = soup.find_all('div', class_='mc-title')
            
            for film in search:
                for element in film.find_all('a'):
                    link = element['href']
                    results.append(link)
            url = results[0]
            
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'lxml')

            runtime = soup.find('dd', itemprop='duration').text
            runtime = runtime.strip(' min.')
            runtime = int(runtime)
            country_name = ''
            country = soup.find('span', id='country-img')
            for cname in country:
                country_name = cname['alt']
            rating = soup.find('div', id='movie-rat-avg').text
            rating = rating.strip()
            rating = rating.replace(',','.')
            rating = float(rating)
            n_ratings = soup.find('span', itemprop='ratingCount').text
            n_ratings = n_ratings.replace('.', '')
            n_ratings = int(n_ratings)
        else:
            runtime = soup.find('dd', itemprop='duration').text
            runtime = runtime.strip(' min.')
            runtime = int(runtime)
            country_name = ''
            country = soup.find('span', id='country-img')
            for cname in country:
                country_name = cname['alt']
            rating = soup.find('div', id='movie-rat-avg').text
            rating = rating.strip()
            rating = rating.replace(',','.')
            rating = float(rating)
            n_ratings = soup.find('span', itemprop='ratingCount').text
            n_ratings = n_ratings.replace('.', '')
            n_ratings = int(n_ratings)
        runtimes.append(runtime)
        countries.append(country_name)
        ratings.append(rating)
        number_ratings.append(n_ratings)
        cont += 1
        progress_bar(cont, total)
    for movie in movie_list:
        titles.append(movie.title)
        movie.year = int(movie.year)
        years.append(movie.year)
        directors.append(movie.director)
    length = len(movie_list)
    df = pd.DataFrame({'Title': titles, 'Year': years, 'Director': directors, 'Runtime (mins.)': runtimes, 'Country': countries, 'Rating on FA': ratings, 'Number of ratings': number_ratings}, index=list(range(1,length+1)))
    df.to_excel('Pelis2021.xlsx', index = False, header = True)
    print(colorama.Fore.RESET)
    print('Done')

def main():
    movies = make_list()
    get_movies_data(movies)

if __name__ == '__main__':
    main()