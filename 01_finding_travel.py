
# coding: utf-8

# In[3]:

import simplejson as json


# In[15]:

def load_cities():
    # loads 1000 cities from a corpora list
    us_cities = json.load(open('./corpora/data/geography/us_cities.json'))
    #print(len(us_cities))
    #print(type(us_cities))
    #print(us_cities.keys())
    city_list = [city['city'] for city in us_cities['cities']]
    return city_list


# In[16]:

city_list = load_cities()
print(len(city_list))


# In[23]:

# search for people driving to the top x cities in the USA
def search_github(city_list):
    search_url_temp = "https://api.github.com/search/code?q=user:GITenberg+%22{0}+to+{1}%22"
    for city in city_list:
        clean_city = city.
        print(search_url_temp.format("drive", city))
    


# In[24]:

search_github(city_list[:5])


# In[ ]:

"".

