import streamlit as st
import pandas as pd

st.title("Analyse du catalogue Netflix")

df = pd.read_csv('netflix_titles.csv')

st.write(f"Nombre total de contenus : {len(df)}")

