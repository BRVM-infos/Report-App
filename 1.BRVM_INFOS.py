# import library
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# set wide mode App
st.set_page_config(layout="wide", page_title= "BRVM" )

df = pd.read_csv('Main_Data')

# Liste des pays de l'UEMOA
country_uemoa = list(df['Pays'].unique())

# Liste des entreprise BRVM
company = list(df['Company Name'].unique())
#st.write(company)

#Créer une dictionnaire pays UEMOA avec leur entreprise respective
pays_company_dict = {}
for i in range(len(df)):
    pays = df.loc[i, 'Pays']
    company_name = df.loc[i, 'Company Name']
    if pays not in pays_company_dict:
        pays_company_dict[pays] = []
    pays_company_dict[pays].append(company_name)

# Eliminer les doublures
country = {}

# Iterate through the dictionary to elimane duplicate vallue
for key, value in pays_company_dict.items():
    # Create a set to store the unique values for this key
    unique_values = set(value)
    # Convert the set back to a list and store it in the new dictionary
    country[key] = list(unique_values)

#st.write(country)

def filter_data(df, country, company):
    filtered_df = df[(df['Pays'] == country) & (df['Company Name'] == company)]
    return filtered_df


def plot_dividende(stock_data, company):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=stock_data['Date'], 
        y=stock_data['Dividende'], 
        mode='lines+markers', 
        marker=dict(color='orange', size=20),  # Adjust marker size here
        line=dict(color='blue'),  # Adjust line color if needed
        name='Dividende'
    ))
    fig.update_layout(
        title=f'Dividende en FCFA de : {company}',
        xaxis_title='Date',
        yaxis_title='Prix FCFA',
        template='plotly_white'
    )
    return fig

def plot_benefice(stock_data, company):
    colors = ['red' if val < 0 else 'blue' for val in stock_data['Résultat net']]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=stock_data['Date'],
        y=stock_data['Résultat net'],
        marker_color=colors
    ))
    fig.update_layout(
        title=f'Bénéfice net de : {company}',
        xaxis_title='Date',
        yaxis_title='Volume',
        template='plotly_white'
    )
    return fig

# Sidebar - Country and Company Selection
countries = country_uemoa
selected_country = st.sidebar.selectbox('Pays', countries)

if selected_country:
    companies = df[df['Pays'] == selected_country]['Company Name'].unique()
    selected_company = st.sidebar.selectbox('Entreprises' , companies)

    # Main content - Centered subheader
    st.markdown(f"""
        <div style="text-align: center;">
            <h2>Dividende et Bénéfice net de :  <span style="color: green;">{selected_company}</span></h2>
        </div>
    """, unsafe_allow_html=True)

    if selected_company:
        filtered_data = filter_data(df, selected_country, selected_company)
        
        # Create columns for side-by-side charts
        col1, col2 = st.columns(2)

         # Plot line chart in the first column
        with col1:
            fig1 = plot_dividende(filtered_data, selected_company)
            st.plotly_chart(fig1)

        # Plot bar chart in the second column
        with col2:
            fig2 = plot_benefice(filtered_data, selected_company)
            st.plotly_chart(fig2)


st.set_option('deprecation.showPyplotGlobalUse', False)

