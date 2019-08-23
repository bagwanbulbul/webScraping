from pprint import pprint
from all_movies_details import*

movie_director = {}
all_director = []
def directors_list(movies_list):
    for index in movies_list:
        director = index["director"]
        all_director.extend(director)
    return all_director
director_data = directors_list(movie_all_data)

def selected_director(movie_director):
    new_list = []
    for index in movie_director:
        if index not in new_list:
            new_list.append(index)
    return new_list
selected = selected_director(all_director)

def analyse_movies_director(selected_director,director_data):
    for director in selected_director:
        index = 0
        count = 0 
        while index<len(director_data):
            particular_director = director_data[index]
            if director == particular_director:
                count = count +1
            index = index+1
        movie_director[director]= count
    return (movie_director)
all_data = analyse_movies_director(selected,director_data)
pprint (all_data)