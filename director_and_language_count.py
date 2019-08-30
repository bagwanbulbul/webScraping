from pprint import pprint 
from Indian_top50_Movies import*
from all_movies_details import*
from director_count import*
new_list = []
def without_duplicate(director_list):
    for index in director_list:
        if index not in new_list:
            new_list.append(index)
    return new_list
data = all_data
without_duplicate_director_list =  (without_duplicate(data))

main_data = {}
def analyse_language_and_directors(movie_list,directors_list):
        for index in directors_list:
                all_language = []
                language_count = {}
                for movie in movie_list:
                        if index in movie["director"]:
                                all_language.extend(movie['language'])
                selected_language =[]
                for particular_language in all_language:
                        if particular_language not in selected_language:
                                selected_language.append(particular_language)
                count = 0
                for same_language in selected_language:
                        for language in all_language:
                                if language == same_language:
                                        count = count +1
                        language_count[same_language] = count
                main_data[index] = language_count
        # pprint (main_data)  
        return main_data       
data = movie_all_data
directors = without_duplicate_director_list
analyse_data = analyse_language_and_directors(data,directors)
# pprint (analyse_data)
