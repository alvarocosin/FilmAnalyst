# Lee una lista de películas desde un .txt y los escribe en una hoja excel
import pandas as pd
from movie import Movie
#Reads movie list file and creates a list from it
with open('pelis2021.txt') as f:
    lines = f.readlines()
f.close()

movies = list()

#Separates movie, year and director from data and makes a movie list
for line in lines:
    line = line.strip()
    firstbreak = line.find('(')
    title = line[2:firstbreak - 1]
    year = line[firstbreak + 1:firstbreak + 5]
    secondbreak = line.find('.')
    director = line[secondbreak + 2:]
    movie = Movie(title=title, year=year, director=director)
    movies.append(movie)
#Crea un csv con los datos 
# length = len(movies)
# df = pd.DataFrame({'Título': movies.title, 'Año': movies.year, 'Director': movies.director}, index=list(range(1,length+1)))
# df.to_csv('Pelis2021.csv', index = False)
# print('Done')