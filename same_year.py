import requests
from pprint import pprint
from bs4 import BeautifulSoup
from Indian_top50_Movies import movieInfo
def sort_list(movies):
        sorted_years = []
        for year in movies:
                str_type_year = (year["year"])
                int_type_year = int(str_type_year[1:5])
                if int_type_year not in sorted_years:
                        sorted_years.append(int_type_year)
        sorted_years.sort()
        return  sorted_years
sorted_years_list = sort_list(movieInfo)
# pprint (sorted_years_list)

group_year = {}
def group_by_year(sameYears,movieslist):
        for same_years in sameYears:
                index = 0
                movie_group_by_year = []
                while index < len(movieslist):
                        str_year =  movieslist[index]["year"]
                        int_year = int(str_year[1:5])
                        if same_years == int_year:
                                movie_group_by_year.append(movieslist[index])
                        index=index+1 
                        group_year[same_years] = movie_group_by_year 
        return group_year
sortedlist = sorted_years_list
moviedetails = movieInfo
sameYearmovielist = group_by_year(sortedlist,moviedetails)
# pprint (sameYearmovielist)





