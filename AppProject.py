# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
# Get the path to the CSV file on Google Drive
#csv_path = "/content/BRVM"
csv_url = 'https://github.com/BRVM-infos/Report-App/blob/main/BRVM.csv'
df = pd.read_csv(csv_url)
