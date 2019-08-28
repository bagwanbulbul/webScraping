from all_movies_details import*
import json
import os.path
from pprint import pprint 
from Indian_top50_Movies import*
import random
import time

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
        movies = []
        for index in movies_list:
                all_url = index["url"]
                fileName = "cachingFiles/"+all_url[28:36]+".json"
                if os.path.exists(fileName):
                    read_data = readingfile(fileName)
                    movies.append(read_data)
                else:
                    movie = scrape_movie_details(all_url)  
                    fileData = movie
                    write_data =  writingFile(fileName, fileData)
                    a = random.randint(1,3)
                    time.sleep(a)
        return movies    
movie_details = get_movie_list_details(movieInfo)
pprint (movie_details)