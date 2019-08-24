# from all_movies_details import*
# pprint (all_movies_details)
import json
import os.path
from pprint import pprint 
from Indian_top50_Movies import*
# from all_movie_details import*

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

def get_movie_list_details(movies_list):
        movie_data=[]
        for index in movies_list:
                all_url = index["url"]
                get_data = requests.get(all_url)
                # pprint (get_data)

                json_data = get_data.json()
                pprint (json_data)

                # fileName = "urls/"+all_url+".json"
                # data = writingFile(fileName, json_data)
                # movie = scrape_movie_details(all_url)
                # movie_data.append(movie)
        return movie_data
movie_all_data = get_movie_list_details(movieInfo)