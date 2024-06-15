# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
import matplotlib.pyplot as plt

# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
st.title('Mon Application Streamlit')
st.write('Chargement des données depuis GitHub...')
df = pd.read_csv("BRVM.csv")
st.write('Voici contenu du fichier CSV :')
st.dataframe(df)
st.bar_chart(df, x="Date", y="Dividende")
# Créer le graphique en barres pour les dividendes
def create_bar_chart(dividendes):
    years = list(dividendes.keys())
    values = list(dividendes.values())

    fig, ax = plt.subplots()
    ax.bar(years, values, color=['brown', 'orange', 'yellow', 'purple', 'magenta'])
    ax.set_xlabel('Année')
    ax.set_ylabel('Dividende en FCFA')
    ax.set_title('Dividende en FCFA')
    return fig
