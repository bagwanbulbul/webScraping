from pprint import pprint
from Indian_top50_Movies import movieInfo
from same_year  import sameYearmovielist 
from same_year import sorted_years_list
movie_decade = {}
def group_by_decade (years,movies):
        for year in years:
                new_list = []
                decade = year%10
                year_decade = year-decade
                decades = year_decade+10
                index = 0
                for index in range(year_decade, decades):
                        if index in years:
                                new_list.extend(movies[index])
                movie_decade[year_decade]=new_list
        return movie_decade
a = sorted_years_list
b = sameYearmovielist 
decade_years = group_by_decade(a,b)
pprint (decade_years)