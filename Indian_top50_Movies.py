import requests
from pprint import pprint
from bs4 import BeautifulSoup
url = " https://www.imdb.com/india/top-rated-indian-movies/"
getData = requests.get(url).text
soup = BeautifulSoup(getData,"html.parser")
Title = soup.find("tbody",class_="lister-list")
trs = Title.findAll("tr")
movies = []
def scrape_top_list(trs):
    position = 1
    for movie in trs:
        movie_details = {}
        name = movie.find("td",class_="titleColumn").a.get_text()
        year = movie.find("span",class_="secondaryInfo").get_text()
        rating = movie.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url = movie.find("a")
        url = "https://www.imdb.com/"+url["href"]
        movie_details["name"]=name
        movie_details["year"]=year
        movie_details["Rating"]=rating
        movie_details["url"]=url
        movie_details["position"]=position
        position=position+1
        movies.append(movie_details)
    return movies
movieInfo = scrape_top_list(trs)
# pprint (movieInfo)


    
