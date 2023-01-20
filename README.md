# FilmAnalyst :movie_camera: :bar_chart:
FilmAnalyst is a tool made in Python to analyze a set of data. In this case it analyzes a list of films watched in a year.

Every year since 2019 I have taken the time to write down every film I watch including its title, year and director. All my lists look something like this:
```bash
- A Serious Man (2009) dir. Joel and Ethan Coen
- North by Northwest (1959) dir. Alfred Hitchcock
- Paths of Glory (1957) dir. Stanley Kubrick
- Come and See (1985) dir. Elem Klímov
- The Northman (2022) dir. Robert Eggers
```
I was curious to see more data regarding every film, like how popular each one is or what film is considered the best among the ones I watched.
So I decided to use web scraping to collect data from a familiar web-site called FilmAffinity (similar to iMDB but for spanish speaking people). 
I used the data I had (title, year, director) and combined it with the data I scraped that I was interested in to write an Excel document.

## Usage :computer:
This script is written in Python and is executed through a terminal command. Basically what this script makes is reading a .txt file that looks like the text I wrote above and separates every line (every film) and every piece of information from the film. Afterwards it scrapes the data from the FilmAffinity site and pairs it with each film.<br> 
Here's how the execution looks like:
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/initial.png)
And here it has finished!
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/finished.gif)


