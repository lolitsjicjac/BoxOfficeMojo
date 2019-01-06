# BoxOfficeMojo
Web Scraper that gets all domestic box office prices of movies on BoxOfficeMojo using links. Google Search is used to get the links from python.

# Step One
Have a csv that has the links to the movies or use the pre built google search to get the links to the specific movie titles that you want.

# Step Two
Do this only is you searched the google site for the movie links. 
Make sure to QA the links the were returned as google sometimes likes to return different movie links since BoxOfficeMojo does not label each movie in a nice fashion. EX: Jurassic World is codename in their link as JurassicSuquel. So be on the look out for this.
If you have located links that should not have been returned used the prebuild function that deletes those values from the list with their specific index location in the link.

# Step Three
Run the BoxOfficeMojo web scraper to get the domestic box office prices of the movies.

# Final Code
The final code should give you a dataframe with the movie title and its respective box office gross and a second dataframe with all the movies and their respective BoxOfficeMojo links.
