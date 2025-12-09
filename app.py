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

