import requests
from bs4 import BeautifulSoup


# get html code using requests
URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
response.raise_for_status()
website_html = response.text

# parse data using bs
soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

# find tags
movie_list = soup.find_all(name='h3', class_='title')

# save to txt file
with open('movies.txt', 'w') as output_file:
    for movie in movie_list[::-1]:
        output_file.write(f"{movie.getText()}\n")
