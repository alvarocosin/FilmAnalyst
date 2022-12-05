# Lee una lista de películas desde un .txt y los escribe en una hoja excel
import openpyxl
from openpyxl.styles import Font

with open('pelis2021.txt') as f:
    lines = f.readlines()
f.close()

movies = list()
years = list()
directors = list()

for line in lines:
    line = line.strip()
    firstbreak = line.find('(')
    movie = line[2:firstbreak - 1]
    movies.append(movie)
    year = line[firstbreak + 1:firstbreak + 5]
    years.append(year)
    secondbreak = line.find('.')
    director = line[secondbreak + 2:]
    directors.append(director)
    print(movie + ' (' + year + ') ' + director)