import pandas as pd
import os
os.system("") 
import streamlit as st

import streamlit_shadcn_ui as ui
#import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


################################
# Page configuration
st.set_page_config(
    page_icon= "🌍",
    layout="wide", 
    page_title= "BRVM",
     initial_sidebar_state="expanded")

#####################################
# Set up css file via fucntion
# Function to load CSS from a file and inject it into the app
def load_css(file_name):
     if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style >{f.read()}</style>', unsafe_allow_html=True)
     else:
        st.error(f"CSS file '{file_name}' not found. Please check the file path.")

# Set the working directory to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
        

# Load the CSS file
load_css('style.css')


# Read csv file
df_main = pd.read_csv('brvm_data.csv')

#st.write(df_main)

#*************Extract unique Ticket and company Name ********

# Extract unique countries and companies
country_uemoa = df_main['Pays'].unique()
company = df_main['Company_Name'].unique()

# Create a dictionary to map each country in UEMOA to its list of unique companies
pays_company_dict = {}
for _, row in df_main.iterrows():
    pays = row['Pays']
    company_name = row['Company_Name']
    if pays not in pays_company_dict:
        pays_company_dict[pays] = set()  # Use set to automatically handle duplicates
    pays_company_dict[pays].add(company_name)

# Convert sets to lists in the dictionary
country = {key: list(value) for key, value in pays_company_dict.items()}




#******************* Définir les fonction graphiques*************

def filter_data(df, country, company):
    filtered_df = df[(df['Pays'] == country) & (df['Company_Name'] == company)]
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
        title=f'Dividende en FCFA',
        xaxis_title='Date',
        yaxis_title='FCFA',
        template='plotly_white'
    )
    return fig

def plot_benefice(stock_data, company):
    colors = ['red' if val < 0 else 'blue' for val in stock_data['Resultat_net']]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=stock_data['Date'],
        y=stock_data['Resultat_net'],
        marker_color=colors
    ))
    fig.update_layout(
        title= f'Bénéfice net',
        xaxis_title='Date',
        yaxis_title='Million FCFA',
        template='plotly_white'
    )
    return fig

#************Side bar, main task of Appp*******

# Sidebar - Country and Company Selection
countries = country_uemoa

selected_country = st.sidebar.selectbox('Pays', countries)

if selected_country:
    companies = df_main[df_main['Pays'] == selected_country]['Company_Name'].unique()
    selected_company = st.sidebar.selectbox('Entreprises' , companies)

    # Metric card
    cart_pays=  df_main[df_main['Company_Name'] == selected_company]['Pays'].unique()
    cart_ceo =  df_main[df_main['Company_Name'] == selected_company]['Profile_Dirigeants_'].unique()
    cart_val =  df_main[df_main['Company_Name'] == selected_company]['Profile_Valorisation_de_la_société_'].unique()
    #***********Metric Card************
   
  
    cols = st.columns(3)
    with cols[0]:
        ui.metric_card(title="Pays", content=f"{cart_pays[0]}", 
                   key="card1")
    with cols[1]:
        ui.metric_card(title="CEO", content=f"{cart_ceo[0]}", 
                   key="card2")
    with cols[2]:
        ui.metric_card(title="Valorisation de la société", content=f"{cart_val[0]}", 
                   key="card3")
    # Main content - Centered subheader
    st.markdown(f"""
                 <div class="title">  {selected_company}  </div> """,
                   unsafe_allow_html=True)

    if selected_company:
        filtered_data = filter_data(df_main, selected_country, selected_company)
        
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
        
         # Create columns for side-by-side charts
        stat, descrip = st.columns(2)

         # metric of companys
        with stat:
         # Title of the section using the custom CSS class
            st.markdown('<div class="section">Statistique</div>', unsafe_allow_html=True)

            # Desciption of company
        with descrip:
             # Title os this section
            st.markdown('<div class="section">Description</div>', unsafe_allow_html=True)
            # Display description content
            resume =  df_main[df_main['Company_Name'] == selected_company]['Description'].unique()[0]
            st.markdown(f"""
                 <div class="resume">  {resume}  </div> """,
                   unsafe_allow_html=True)

            
st.set_option('deprecation.showPyplotGlobalUse', False)


