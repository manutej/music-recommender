
import streamlit as st
import pickle
import pandas as pd

@st.cache(show_spinner=False)
def open_pickles():
    #with open('dict.pkl','rb') as f:
        #artist_dict = pickle.load(f)
    with open('artist_df.pkl','rb') as f2:
        artist_df = pickle.load(f2)
    return artist_df
artist_df = open_pickles()
#artist = "the beatles"
def process_artist(artist_name):
    return artist_name.replace(" ","+")

def get_json(artist):
    
    api_key = "c57c3bebabde1412074c0c52a90cc0ad"
    artist_url = process_artist(artist)
    url = f"https://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_url}&api_key={api_key}&format=json"
    import requests
    res = requests.get(url)
    res_json = res.json()
    return res_json

def get_headline(artist_json):
    headline = artist_json['artist']['bio']['summary'].split('<a')[0]
    return headline


st.title('Music Recommender System')
st.header('Finding new artists based on the artists you love')
st.subheader('Choose an artist to explore other related Artist?')

with st.form('scrivener'):
    artist = st.text_input('Artist Name', 'Enter the artist name here')
    

    if st.form_submit_button('Analyze!'):
        txt = artist.lower().strip()
        #st.write('The current artist selected is', artist)
        st.write('Here are the top 10 related artists for your selection of ', artist.capitalize())
        #top10 = [st.write(art) for art in artist_dict[txt]['top10']]
        top10 = list(artist_df.loc[txt,'top10'].index)
        for artist in top10:
            
            artist_json = get_json(artist)
            st.subheader(artist)
            st.write(get_headline(artist_json))


        #st.write(top10)
    if len(artist) == 0:
      st.write('You must include an artist in the input for recommendation.')
    
      #pred = model.predict([txt])[0]
      #st.write('You write like', pred)