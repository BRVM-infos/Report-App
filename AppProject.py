# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
url_csv = "https://github.com/BRVM-infos/Report-App/blob/main/BRVM.csv"
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifier les erreurs de requête
        csv_content = response.content
        df = pd.read_csv(pd.compat.StringIO(csv_content.decode('utf-8')))
        return df



   

