

# Music Recommender System

## Music Recommender System Project published on Streamlit

### Purpose: 

The goal for this project was to develop a comprehensive music recommender system that is able to take in an input of an artist and generate 10 similar recommendations of musical artists. The recommender system will be a collaborative filtering recommender model that uses information about the number of plays for certain artists across users served in a web application. This is an application of machine learning that allows discovery of new musical artists based on existing data. 


## File Structure
The file directory for this repository does not contain the original data, which can be found [here](http://ocelma.net/MusicRecommendationDataset/lastfm-360K.html). There are 3 key scripts/notebooks. The first is for loading the data for processing and sampling, which is a python script that can be run from the terminal. The second file is a jupyter notebook for exploring the output from the first script to get a better understanding of the data through exploratory data analysis. The final file is for the Streamlit application that will serve the website to a local web application. The images folder contains the output images of the Exploratory Data Analysis in the jupyter notebook. Finally, the presentation used for this project is also included in this github repository for review of more details about the project.

3 main notebooks are: 

1) 01_load_results.py
2) 02_eda.ipynb
3) 03_music_app.py

## The process of the work:

1) Gather Data 
- Data was found from a scrape of the Last.FM API hosted [here.](http://ocelma.net/MusicRecommendationDataset/lastfm-360K.html)
2) Data Cleaning and Processing - Building Recommender data
- The 01_load_results script loads the data and processes the data. In order to account for memory limitations on a local machine, the data was subsampled to 300,000 rows. The pivot_tables method breaks at sizes larger than this, so this was a workable sample size that was used for this project.
3) Exploratory Data Analysis (EDA)
- The exploratory data analysis involved reviewing the top number of plays, average number of plays, and number of ratings, which were the 3 numerical columns in our data acquired from the data processing. 
4) Building Web Application
- For this recommender, streamlit services were used to surface a web application that is able to use the data processed in the first script in order to surface results. Also, the LastFM API was used to be able to load summaries of artist profiles upon loading of results.
5) Making Conclusions about our Findings
- A presentation was created that can be found in this github repository.

## Methodology:

Recommender systems using collaborative filtering use data across different users to determine the similarity score (via pairwise distances) between two entities (e.g. artists). While the traditional case may use ratings or sentiments, this recommender system used number of plays for a given artist by a given user. This was a numerical metric that was then used to compute distances between artists in order to build the recommender model. Once the distances were calculated, scores for each artist were used to generate the top 10 artists for each artist. Finally, this information was loaded into a dictionary that defined top 10 artists for each artist, the average number of plays, total number of plays, and total number of ratings. "Ratings" in this case is defined as 1 set of plays for a given user. 

Then, this dictionary was saved by pickling to be loaded into the following application by streamlit. The streamlit application uses relatively boilerplate code that allows user to input one musical artist in order to find 10 related artists. Last.FM API was also used to populate a brief artist profile for each artist that would be loaded into the results of the recommender. 


## Discussions/Conclusions

The music recommender developed here was an initial prototype and could be improved in several ways. For one, the sample used to generate this recommender only contained a fraction of all of the data provided by our data set. Because of limitations in memory and computational resources, it proved to be more reasonable to only use a subset of the rows. In its current version, the streamlit app only loads a local instance rather than a web-hosted application. This is planned to be corrected in future versions. 

This music recommendation system was shown to be succesfully able to generate artist recommendations using the Last.FM dataset of user and artist data. 

Work by 
Manutej Mulaveesala
