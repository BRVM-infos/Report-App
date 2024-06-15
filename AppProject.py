# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st
import requests
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
def create_bar_chart(dividendes):
    years = list(dividendes.keys())
    values = list(dividendes.values())

    fig, ax = plt.subplots()
    ax.bar(years, values, color=['brown', 'orange', 'yellow', 'purple', 'magenta'])
    ax.set_xlabel('Année')
    ax.set_ylabel('Dividende en FCFA')
    ax.set_title('Dividende en FCFA')
    return fig
data = df
companies = data['Ticket'].tolist()

st.write("### Sélectionnez une entreprise :")
cols = st.columns(len(companies))

selected_company = st.session_state.get('selected_company', companies[0])

    # this loop display each company logo once and allow to store eacht company Ticket once
for i, company in enumerate(companies):
        with cols[i]:
            if st.button(company, key=f"button_{i}"):
                st.session_state['selected_company'] = company
                selected_company = company
            logo_url = data[data['Ticket'] == company]['Profile.Images'].values[0]
            st.image(logo_url, width=100)

st.write(f"## Données pour {selected_company}")
  #Store each company Ticke once
company_data = data[data['Ticket'] == selected_company].iloc[0]

st.pyplot(create_bar_chart(company_data['Dividende']))
