# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 16:47:08 2019

@author: albertocas
"""

import pandas as pd
import BoxOfficeMojoFunctions as bo


##Using google to scrap the box office mojo movie links
##Here you should link your new links that is produced at the end of the script
links = "C:/Users/albertocas/Documents/Python/Movio_Links.csv"
#Here you will link your new movies that will be added  
new_movie = "C:/Users/albertocas/Documents/Movio/New_Movio_Titles_1.3.19.csv"

Movio_Domestic = pd.DataFrame({"Link to BoxOfficeMojo": [], "Movie": [] , "Domestic Box Office in Millions": []})
movio_links = pd.read_csv(links) #header = None, names = ["Link to BoxOfficeMojo", "Movie"])
new_movio_names = pd.read_csv(new_movie)


#Getting the newest links
boxsearch = "Box Office Mojo"
Lastsearch = "Gross Domestic"
real_links = bo.google_search_new_movies(new_movio_names["movie_title"],boxsearch)

#this will update the links so we only are left with the corect ones
bo.delete_values_in_list(real_links, [6] ,len(real_links))

#Get the domestic prices of the new movies
domestic_price_list = bo.boxofficemojo_new_movies(real_links)

#updating all of the old movio movies
domestic_price_list_movio = bo.boxofficemojo(movio_links["Link to BoxOfficeMojo"])

#Setting them to the DF
movio_links["Domestic Box Office in Millions"] = domestic_price_list_movio



#Now we populate our data frame that we created in the beginning to have the final values for
#all the new movies.
Movio_Domestic["Domestic Box Office in Millions"] = domestic_price_list
Movio_Domestic["Movie"] = new_movio_names["movie_title"]
Movio_Domestic["Link to BoxOfficeMojo"] = real_links

Movio_UTD = movio_links.append(Movio_Domestic, ignore_index = True)
Movio_UTD = Movio_UTD.sort_values(["Movie"]).reset_index().drop("index", axis = 1)

#Without links
Movio_UTD_no_links = Movio_UTD.copy().drop("Link to BoxOfficeMojo", axis =1 )


#Need the new links for the future
Movio_UTD_Links = Movio_UTD.copy()
Movio_UTD_Links = Movio_UTD_Links.drop("Domestic Box Office in Millions", axis = 1)



###################### TO CSV RUN AFTER QA ####################################
#
#Movio_UTD_no_links.to_csv("Movio_Domestic.csv", index = False)
#Movio_UTD_Links.to_csv("Movio_Links.csv", index = False)