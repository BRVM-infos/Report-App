# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
csv_url = "https://github.com/BRVM-infos/Report-App/blob/main/BRVM.csv"
response = requests.get(csv_url)
csv_content = response.content

# Utiliser pandas pour lire le contenu CSV
df = pd.read_csv(pd.compat.StringIO(csv_content.decode('utf-8')))
