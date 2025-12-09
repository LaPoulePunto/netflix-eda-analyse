import streamlit as st
import pandas as pd

st.title("Analyse du catalogue Netflix")

df = pd.read_csv('netflix_titles.csv')

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

erroneous_ratings = ['74 min', '84 min', '66 min']
df = df[~df['rating'].isin(erroneous_ratings)].copy()
df['country'] = df['country'].fillna('Unknown')

col1, col2, col3 = st.columns(3)
col1.metric("Total", len(df))
col2.metric("Films", len(df[df['type'] == 'Movie']))
col3.metric("Séries", len(df[df['type'] == 'TV Show']))

st.header("Films vs Séries")

type_counts = df['type'].value_counts()
st.bar_chart(type_counts)

st.header("Filtres")

type_filter = st.multiselect("Type", df['type'].unique(), default=df['type'].unique())
year_range = st.slider("Année de sortie", 
                       int(df['release_year'].min()), 
                       int(df['release_year'].max()),
                       (int(df['release_year'].min()), int(df['release_year'].max())))

df_filtered = df[(df['type'].isin(type_filter)) & 
                 (df['release_year'] >= year_range[0]) & 
                 (df['release_year'] <= year_range[1])]

st.header("Genres")

from collections import Counter

all_genres = []
for genres in df_filtered['listed_in'].dropna():
    genre_list = [g.strip() for g in str(genres).split(',')]
    all_genres.extend(genre_list)

genre_counts = Counter(all_genres)
top_genres = pd.DataFrame(genre_counts.most_common(10), columns=['Genre', 'Nombre'])

st.bar_chart(top_genres.set_index('Genre'))

st.header("Pays")

all_countries = []
for countries in df_filtered['country']:
    country_list = [c.strip() for c in str(countries).split(',')]
    all_countries.extend(country_list)

country_counts = Counter(all_countries)
top_countries = pd.DataFrame(country_counts.most_common(15), columns=['Pays', 'Nombre'])

st.bar_chart(top_countries.set_index('Pays'))

