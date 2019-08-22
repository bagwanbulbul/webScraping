from pprint import pprint 
from Indian_top50_Movies import*
from movie_details import*
movie_data=[]
def get_movie_list_details(movies_list):
        for index in movies_list[:10]:
                all_url = index["url"]
                movie = scrape_movie_details(all_url)
                movie_data.append(movie)
        return movie_data
movie_all_data = get_movie_list_details(movieInfo)
pprint (movie_all_data)

