from pprint import pprint 
from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
getData = requests.get(url).text
soup = BeautifulSoup(getData,"html.parser")
table = soup.find("table",class_="cast_list")
trs = table.find_all("tr")
# pprint (trs)

data = []
def scrape_movie_cast(movie_caste_url):
    for index in movie_caste_url:
        # pprint (index)
        details = {}
        name = index.find("tr",class_="odd")
        a = name.find("td",class_="primary_photo").a["href"]
        pprint (a)





# url = "https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
movie_cast = scrape_movie_cast(trs)