import requests
from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

URL = "https://time.com/6341118/best-movies-2023/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
# print(movie_titles[::-1])
# for n in range(len(movie_titles) 1, 0, -1):
#     print(movie_titles[n])
with open("45.6.MoviesScraping\\movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

    
