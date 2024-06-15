# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests

# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
st.title('Mon Application Streamlit')
st.write('Chargement des données depuis GitHub...')
df = pd.read_csv("BRVM.csv")
st.write('Voici contenu du fichier CSV :')
st.dataframe(df)
st.bar_chart(df, x="Date", y="Dividende")
st.line_chart(df, x="Date", y="Dividende")
