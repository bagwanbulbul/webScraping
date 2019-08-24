from all_movies_details import*
import json
import os.path
from pprint import pprint 
from Indian_top50_Movies import*
from all_movies_details import*

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
                fileName = "cachingFiles/"+all_url[28:36]+".json"
                if os.path.exists(fileName):
                        data = readingfile(fileName)
                        return data
                else:
                        movie = scrape_movie_details(all_url)  
                        fileData = movie
                        data =  writingFile(fileName, fileData)
                        return data

        # return data
movie_details = get_movie_list_details(movieInfo)
pprint (movie_details)


