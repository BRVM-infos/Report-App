# prompt: give code allow to read csv file with pandas data frame

import pandas as pd
import streamlit as st

# Get the path to the CSV file on Google Drive
csv_path = "/content/BRVM"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_path)

# Print the DataFrame
#df.head()
# Créer le graphique en barres pour les dividendes
def create_bar_chart(dividendes):
    years = list(dividendes.keys())
    values = list(dividendes.values())

    fig, ax = plt.subplots()
    ax.bar(Date, values, color=['brown', 'orange', 'yellow', 'purple', 'magenta'])
    ax.set_xlabel('Année')
    ax.set_ylabel('Dividende en FCFA')
    ax.set_title('Dividende en FCFA')
    return fig

# Créer le graphique en ligne pour le bénéfice net
def create_line_chart(resultat_net):
    years = list(resultat_net.keys())
    values = list(resultat_net.values())

    fig, ax = plt.subplots()
    ax.plot(Date, values, marker='o', color='cyan')
    ax.set_xlabel('Année')
    ax.set_ylabel('Bénéfice Net (Million en FCFA)')
    ax.set_title('Bénéfice Net (Million en FCFA)')
    return fig
# Interface utilisateur
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

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(create_bar_chart(company_data['Dividende']))
    with col2:
        st.pyplot(create_line_chart(company_data['R\u00e9sultat net']))
