# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
csv_url = 'https://github.com/BRVM-infos/Report-App/blob/main/BRVM.csv'
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifier les erreurs de requête
        csv_content = response.content
        df = pd.read_csv(pd.compat.StringIO(csv_content.decode('utf-8')))
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la requête HTTP : {e}")
        return None
    except pd.errors.ParserError as e:
        st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
        return None

st.title('Mon Application Streamlit')
st.write('Chargement des données depuis GitHub...')
df = load_data(csv_url)

if df is not None:
    st.write('Voici les premières lignes du fichier CSV :')
    st.dataframe(df.head())
else:
    st.error('Impossible de charger les données.')
