from pprint import pprint
from movie_caching import*

def analyse_actors (movies_list):
        cast_name = []
        for index in movies_list:
                name_key = index["cast"]
                key = {}
                for i in name_key:
                        id = i["imdb_id"]
                        name = i["name"]
                        cast_name.append(name)
                whiout_duplicat = []
                for name in cast_name:
                        if name not in whiout_duplicat:
                                whiout_duplicat.append(name)
               
                main_data = {}
                for cast in whiout_duplicat:
                        count = 0
                        for j in cast_name:
                                if cast == j:
                                        count = count +1
                        main_data["name"]=cast
                        main_data["num_movies"]=count
                        key[id]=main_data
                pprint(key)
analyse_data = analyse_actors(movie_details)