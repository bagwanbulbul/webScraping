from pprint import pprint
from all_movies_details import*

movie_language = {}
all_languages = []
def languages_list(movies_list):
    for index in movies_list:
        language = index["genre"]
        all_languages.extend(language)
    return all_languages
language_data = languages_list(movie_all_data)

def selected_language(movie_language):
    new_list = []
    for index in movie_language:
        if index not in new_list:
            new_list.append(index)
    return new_list
selected = selected_language(all_languages)

def analyse_movies_language(selected_language,language_data):
    for language in selected_language:
        index = 0
        count = 0 
        while index<len(language_data):
            particular_language = language_data[index]
            if language == particular_language:
                count = count +1
            index = index+1
        movie_language[language]= count
    return (movie_language)
all_data = analyse_movies_language(selected,language_data)
pprint (all_data)