# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:35:30 2019

@author: albertocas
"""

import requests
from bs4 import BeautifulSoup as bs
import re
import googlesearch
from googlesearch import search
import urllib.request

def delete_values_in_list(list_to_delete, index_of_values_to_delete, length_of_list_to_delete):
    """
    This will remove values from the list_to_delete. You give it the specific index
    that the values you want to delete from that list are. This will manipulate that initial
    list. This is handy for quick small list.
    """
    while length_of_list_to_delete == len(list_to_delete):
        del list_to_delete[index_of_values_to_delete[0]]
    else:
        for value in index_of_values_to_delete[1:]:
            del list_to_delete[value - (length_of_list_to_delete - len(list_to_delete))]

def count_of_none_value(a_list):
    """
    Used to count the amount of NONE values that are present in a list
    """
    count = 0
    for value in a_list:
        if value == None:
            count += 1
    return count

def update_none_with_domestic(a_list, df_col):
    """
    The web scraper likes to return NONE for some values but if you run them
    again it will give you the correct answers. So this will loop until all
    NONE values have been updated
    """
    while count_of_none_value(a_list) != 0:
        for index,value in enumerate(a_list):
            if value == None:
                a_list[index] = domesticboxoffice(df_col[index])
        print("This many None values remain %d. Let me keep updating for you ~~" % count_of_none_value(a_list))
    else:
        print("All None values have been updated ~~")


def domesticboxoffice(url):
    """
    This will scrape the box office of all the movies with a provided link from
    box office mojo
    """
    link = requests.get(url)
    #html = urlopen(link).read()
    soup = bs(link.content, "lxml")
    boxoffice = soup.select("tr b")
    for i in range(len(boxoffice)):         
        if "Domestic:" in boxoffice[i]:
            index = i+1
            price = re.sub("\D", "", str(boxoffice[index]))
            return "{:.2f}".format(round((float(price)/1000000),2))     
        
def boxofficemojo(df_col):
    """
    This is used to update the old movio links in case some gain more domestic
    box office from the month befores update
    """
    domestic_price_list_movio = []
    for link in df_col:
        domestic_price_list_movio.append(domesticboxoffice(link))
    update_none_with_domestic(domestic_price_list_movio, df_col)
    return domestic_price_list_movio

def google_search_new_movies(df_col, search_after_word = None):
    list_of_links = []
    real_links = []
    for name in df_col:
        for result in search(name+ " "+ search_after_word, tld = "com.pk", lang = "en", num = 2  , start = 0, stop = 2, pause = 2):
            list_of_links.append(result)
    for index, link in enumerate(list_of_links):
        if "https://www.boxofficemojo.com/movies/?id=" in link:
            real_links.append(link)
    return real_links
