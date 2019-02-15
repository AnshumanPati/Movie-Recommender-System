from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'

r = requests.get(url)
bs = BeautifulSoup(r.text,features="lxml")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]
#genres = 
thumbnail = [a.attrs.get('src') for a in soup.select('td.posterColumn a')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    #movie_genres = movie.find('span','genre').findAll('a')
    #movie_genres = [g.contents[0] for g in movie_genres]
    year = re.search('\((.*?)\)', movie_string).group(1)
    #rating = movie.find('span','value').contents[0]
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            #"genre": movie_genres[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
	print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])