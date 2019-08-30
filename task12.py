from pprint import pprint 
from bs4 import BeautifulSoup
from Indian_top50_Movies import*
import requests
import json
import os.path

# url = "https://www.imdb.com/title/tt0066763/"
def get_data_url(url):
        getData = requests.get(url).text
        soup = BeautifulSoup(getData,"html.parser")
        div = soup.find("div",class_="article",id="titleCast")
        second_div = div.find("div",class_="see-more")
        movie_name_id = second_div.find("a")["href"]
        main_url = url+movie_name_id
        return main_url



def writingFile(fileName, fileData):
        file = open(fileName, "w")
        dumps_data = json.dumps(fileData)
        file.write(dumps_data)
        file.close()

def readingfile(fileName):
        file = open(fileName, "r")
        data_file = file.read()
        load_file = json.loads(data_file)  # dict type
        return load_file

def scrape_movie_cast(movie_caste_url):
        url = movie_caste_url
        movie_cast = []
        movie_url =  get_data_url(url)
        getData = requests.get(movie_url).text
        soup = BeautifulSoup(getData,"html.parser")


        table = soup.find("table",class_="cast_list")
        trs = table.find_all("tr")
        odd_tr=table.find_all("tr",class_="odd")
        even_tr= table.find_all("tr",class_="even")

        fileName = "idFiles/"+url[27:36]+".json"
        for index in odd_tr:
                dic = {}
                id =index.a["href"]
                imdb_id = id[5:]
                name = index.img["alt"]
                dic["imdb_id"]=imdb_id
                dic["name"]=name
                movie_cast.append(dic)
        for index1 in even_tr:
                dic = {}
                id = index1.a["href"]
                imdb_id = id[5:]
                name = index1.img["alt"]
                dic["imdb_id"]=imdb_id
                dic["name"]=name
                movie_cast.append(dic)
        if os.path.exists(fileName):
                read_data = readingfile(fileName)
                return read_data
                # pprint (read_data)
        else:
                fileData = movie_cast
                write_data =  writingFile(fileName, fileData)
                return write_data
                        # pprint (write_data)
        # re
url = "https://www.imdb.com/title/tt0066763/"
scrape_cast = scrape_movie_cast(url)
# pprint (scrape_cast)
