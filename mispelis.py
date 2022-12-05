# Lee una lista de películas desde un .txt y los escribe en una hoja excel
import pandas as pd
#Reads movie list file and creates a list from it
with open('pelis2021.txt') as f:
    lines = f.readlines()
f.close()

movies = list()
years = list()
directors = list()

#Separates data from the movie, year and director and makes a list from each one
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

#Crea un csv con los datos 
length = len(movies)
df = pd.DataFrame({'Título': movies, 'Año': years, 'Director': directors}, index=list(range(1,length+1)))
df.to_csv('Pelis2021.csv', index = False)
print('Done')