from pprint import pprint
import requests
from bs4 import BeautifulSoup
movie = {}
url = "https://www.imdb.com/title/tt0093603/"


def get_requests(url):
    respons = requests.get(url).text
    soup1 = BeautifulSoup(respons, "html.parser")
    return soup1


def get_title_data(soup):
    div = soup.find("div", class_="title_wrapper").h1.get_text()
    split1 = div.split()
    name = " ".join(split1[:-1])

    time = soup.find("div", class_="title_wrapper").time["datetime"]
    runtime = time[2:5]

    image = soup.find("div", class_="poster")
    poster_url = image.img["src"]

    movie["name"] = name
    movie["runtime"] = runtime
    movie["poster_url"] = poster_url


def get_bio(soup):
    summary_div = soup.find("div", class_="plot_summary_wrapper")
    summary = summary_div.find("div", class_="plot_summary")
    summary_txt = summary.find("div", class_="summary_text").get_text()
    bio = summary_txt.strip("\n ")
    movie["bio"] = bio


def get_genre_and_director(soup):
    genre_div = soup.find("div", class_="article", id="titleStoryLine")
    all_genre = genre_div.find_all("div", class_="see-more inline canwrap")

    director_div = soup.find("div", class_="credit_summary_item")
    all_director = director_div.find_all("a")
    director_name = []
    for i in all_director:
        director_name.append(i.get_text())

    for index in all_genre:
        movie_genre = index.text
        if "Genres" in movie_genre:
            find_genre = index.find_all("a")
            genre = []
            for i in find_genre:
                genre.append(i.get_text())

    movie["director"] = director_name
    movie["genre"] = genre


def scrape_movie_details(movie_url):

    BeautifulSoup_data = get_requests(movie_url)

    title = get_title_data(BeautifulSoup_data)

    summary = get_bio(BeautifulSoup_data)

    director_and_genre = get_genre_and_director(BeautifulSoup_data)

    div = BeautifulSoup_data.find("div", class_="article", id="titleDetails")
    details = div.find_all("div", class_="txt-block")

    for index in details:
        movie_details = index.text
        if "Country" in movie_details:
            country = index.a.get_text()
        if "Language" in movie_details:
            movie_language = index.find_all("a")
            language = []
            for i in movie_language:
                language.append(i.get_text())
    movie["country"] = country
    movie["language"] = language
    new_movie = movie.copy()
    movie.clear()
    return new_movie
# url = "https://www.imdb.com/title/tt0093603/"
# movie_details = scrape_movie_details(url)
# pprint (movie_details)
