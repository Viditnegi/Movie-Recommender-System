import streamlit as st
import pickle
import requests    # for api


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=15cef82e573ab34e8c4ce203bfc7eacb'.format(movie_id))\
    # data = response.json()   # convert to json

    path = "https://image.tmdb.org/t/p/original/" + response.json()['poster_path']
    return path
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]  # list of Similarities of all movies with this one.
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_posters = []
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.title[i[0]])
        movie_id = movies.movie_id[i[0]]
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters



similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')


movies = pickle.load(open('movies.pkl','rb'))


selected_movie_name= st.selectbox(
    'Select a movie',
    movies['title'].values)


if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5,gap= "medium")
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])