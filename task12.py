from pprint import pprint 
from bs4 import BeautifulSoup
import requests
import json
import os.path

url = "https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
getData = requests.get(url).text
soup = BeautifulSoup(getData,"html.parser")
table = soup.find("table",class_="cast_list")
trs = table.find_all("tr")
tr1=table.find_all("tr",class_="odd")
tr2 = table.find_all("tr",class_="even")

def scrape_movie_cast(movie_caste_url):
        movie_cast = []
        for index in tr1:
                dic = {}
                id =index.a["href"]
                imdb_id = id[5:]
                name = index.img["alt"]
                dic["imdb_id"]=imdb_id
                dic["name"]=name
                movie_cast.append(dic)
        for index1 in tr2:
                dic = {}
                id = index1.a["href"]
                imdb_id = id[5:]
                name = index1.img["alt"]
                dic["imdb_id"]=imdb_id
                dic["name"]=name
                movie_cast.append(dic)
        pprint (movie_cast)
url = "https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
scrape_cast = scrape_movie_cast(url)
# pprint (scrape_cast)
