import requests
import re


# get json data using requests
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)

# use regex to find title
movie_list = []
for title in re.findall(r'"titleText":"(.*?)",', str(response.content)):
    if title not in movie_list:
        movie_list.append(title)

with open('movies2.txt', 'w') as output_file:
    for movie in movie_list[::-1]:
        output_file.write(f"{movie}\n")