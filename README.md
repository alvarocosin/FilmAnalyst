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
<br> Here's how the execution looks like:
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/initial.png)
<br> And here it has finished!
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/finished.gif)
<br> The result is an .xlsx file with all the data I had written plus the data I scraped from the FilmAffinity site. Using Pandas library it's clearly divided by columns and headers for each one. <br>
<br> The excel file look like this in LibreOffice:
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/libreoffice.png)

## Final result :chart_with_upwards_trend:
Finally, I use Microsoft Office Excel to turn the data into a table, which I can filter and sort easily. Also I insert subtables and charts to analyze a particular piece of data which I am interested in a clearer way. <br>
<br> Here is the final excel document:
![](https://raw.githubusercontent.com/alvarocosin/Mispelis/main/resources/excel.png)

