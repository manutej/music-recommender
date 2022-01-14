import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity
import pickle

columns = ['user_id','artist_id','artist_name','n_plays']
print("Loading Data...")
df = pd.read_csv('./lastfm-data/usersha1-artmbid-artname-plays.tsv',
                 names = columns,
                 delimiter = '\t')
print("Data Loaded...")
df.dropna(inplace=True)
print("Data Cleaning Complete...")
#sample = df.sample(n=200000,random_state=42)
sample = df.head(300000)
print('Generating Pivot Table...')
pivot = pd.pivot_table(sample, index='artist_name', columns='user_id', values='n_plays')

sparse_pivot = sparse.csr_matrix(pivot.fillna(0))
print("Pivot table Complete.")
print("Calculating pairwise distance...")
dists = pairwise_distances(sparse_pivot, metric='cosine')
similarities = 1 - dists
print("Generating Recommender DataFrame")
recommender_df = pd.DataFrame(similarities, 
                              columns=pivot.index, 
                              index=pivot.index)
print("Comleted Dataframe")
print(recommender_df.head())

print("Writing results dictionary...")
new_dict = {}
for col in recommender_df.columns:
    #artist = pivot[pivot.index.str.contains(search)].index
    #new_dict[col] = recommender_df[artist].sort_values(ascending = False)[1:11]
    #ORRRR
    new_dict[col] = {
        'top10' : recommender_df[col].sort_values(ascending = False)[1:11],
        'Average Number of Plays': pivot.loc[col, :].mean(),
        'Total Number of Plays': pivot.loc[col, :].sum(),
        'Number of ratings': pivot.T[col].count()
    }
#Pickle this and try to work with that for streamlit, etc
print("Completed Dictionary Write.")
print("Saving Dictionary data to Pickle file...")
with open('dict.pkl','wb') as f:
    pickle.dump(new_dict,f)
print("Results Load Complete. Script will now end.")
