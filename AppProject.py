# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
import numpy as np
#pip install matplotlib
#import matplotlib.pyplot as plt

# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
st.title('Mon Application Streamlit')
st.write('Chargement des données depuis GitHub...')
df = pd.read_csv("BRVM.csv")
st.write('Voici contenu du fichier CSV :')
st.dataframe(df)
st.bar_chart(df, x="Date", y="Dividende")
# Créer le graphique en barres pour les dividendes

data = df
companies = data['Ticket'].tolist()

st.write("### Sélectionnez une entreprise :")
cols = st.columns(len(companies))

selected_company = st.session_state.get('selected_company', companies[0])

st.button(companies[0])
st.session_state['selected_company'] = companies[0]
elected_company = companies[0]
logo_url = data[data['Ticket'] == companies[0]]['Profile.Images'].values[0]
st.image(logo_url, width=100)

st.write(f"## Données pour {selected_company}")
  #Store each company Ticke once
df2 = pd.read_csv("BRVM")
st.write('Voici contenu du fichier CSV :')
st.dataframe(df2)

