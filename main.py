import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def recommend_anime(anime):
    anime_index = animes[animes['Name'] == anime].index[0]
    anime_list = sorted(list(enumerate(similarity[anime_index])), reverse=True, key=lambda x: x[1])[0:6]
    recommended_anime = []
    for i in anime_list:
        recommended_anime.append(f'{animes.iloc[i[0]].Name} ---- Rating: {animes.iloc[i[0]].Rating}')
    return recommended_anime


similarity = pickle.load(open('AnimeRecommender/similarity.pkl', 'rb'))
animes = pd.read_csv('AnimeRecommender/Anime_data.csv')
st.title('Anime Recommendation System')
selected_anime = st.selectbox('Name any Anime..', animes['Name'].values)

if st.button('Recommend'):
    recom = recommend_anime(selected_anime)
    for i in recom:
        st.write(i, unsafe_allow_html=True)
