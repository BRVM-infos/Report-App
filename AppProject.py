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

# Read the CSV file into a Pandas DataFrame
#df = pd.read_csv('BRVM_csv')

# Print the DataFrame
#df.head()
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


def main():
    st.title('Analyse Financière des Entreprises')
    st.markdown('<style>body{background-color: lightgrey;}</style>', unsafe_allow_html=True)

    data = df
    companies = data['Ticket'].tolist()

    st.write("### Sélectionnez une entreprise :")
    cols = st.columns(len(companies))

    selected_company = st.session_state.get('selected_company', companies[0])
    
    # this loop display each company logo once and allow to store eacht company Ticket once
    for i, company in enumerate(companies):
        with cols[i]:
            if st.button(company):
                st.session_state['selected_company'] = company
                selected_company = company
            logo_url = data[data['Ticket'] == company]['Profile.Images'].values[0]
            st.image(logo_url, width=100)

    st.write(f"## Données pour {selected_company}")
  #Store each company Ticke once
    company_data = data[data['Ticket'] == selected_company].iloc[0]

        st.pyplot(create_bar_chart(company_data['Dividende']))
   
