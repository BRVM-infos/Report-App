import pandas as pd
import os
os.system("") 
import streamlit as st

import streamlit_shadcn_ui as ui
#import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
#import base64


################################
# Page configuration
st.set_page_config(
    page_icon= "🌍",
    layout="wide", 
    page_title= "BRVM",
     initial_sidebar_state="expanded")


####################################
#st.header("BRVM") TO HIDDE FOOTER RUNNINF
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True) 

#####################################   
from streamlit_option_menu import option_menu
# horizontal Menu
app = option_menu(None, ["Acceuil", "Tendances", "Dividende", 'Etats Financier', 'Contact'], 
icons=['house', 'fire', "calculator-fill", 'graph-up-arrow', 'person-vcard-fill'], 
menu_icon="cast", default_index=0, orientation="horizontal")
#app

###################################
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
company = df_main['Ticket'].unique()

# Create a dictionary to map each country in UEMOA to its list of unique companies
pays_company_dict = {}
for _, row in df_main.iterrows():
    pays = row['Pays']
    company_name = row['Ticket']
    if pays not in pays_company_dict:
        pays_company_dict[pays] = set()  # Use set to automatically handle duplicates
    pays_company_dict[pays].add(company_name)

# Convert sets to lists in the dictionary
country = {key: list(value) for key, value in pays_company_dict.items()}




#******************* Définir les fonction graphiques*************

def filter_data(df, country, company):
    filtered_df = df[(df['Pays'] == country) & (df['Ticket'] == company)]
    return filtered_df



def plot_benefice(stock_data, company):
    colors = ['red' if val < 0 else 'green' for val in stock_data['Resultat_net']]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=stock_data['Date'],
        y=stock_data['Resultat_net'],
        marker_color=colors
    ))
    fig.update_layout(
      #  title=f'Bénéfice net',
       title = {'text': "Bénéfice net", 
                            'font': {'color': 'lightgrey', 'size': 18} },
        xaxis_title='Date',
        yaxis_title='Million Fcfa',
        template='plotly_white',
         plot_bgcolor='rgba(0, 0, 0, 0.1)',  # Plot area background color
        paper_bgcolor='rgba(0, 0, 0, 0.1)' # Overall background color
    )
    return fig

#************Side bar, main task of Appp*******

# Sidebar - Country and Company Selection
countries = country_uemoa

cols = st.columns([0.15, 0.85], gap='medium')
#### go function 
def go():

    with cols[0]:
        selected_country = st.selectbox('Pays', countries)

        if selected_country:
         companies = df_main[df_main['Pays'] == selected_country]['Ticket'].unique()
         selected_company = st.selectbox('Entreprises' , companies)
    return  selected_country, selected_company
box = list(go())
selected_country = box[0]
selected_company = box[1]
with cols[1]:
    c1, c2 = st.columns(2)
    with c1 :
      
    #st.write(type(box))
     stock_data = filter_data(df_main, box[0], box[1])
     #st.write(stock_data)
     fig = px.scatter(stock_data, x=stock_data['Date'], y=stock_data['Dividende'],
                      title='Dividende en Fcfa',
                 labels={'X': 'X Axis Label', 'Y': 'Y Axis Label'},
                 template='plotly_white',  # Dark theme template
                 color='Dividende',
                 size= 'Dividende'
                 )
     # Add lines to the scatter plot
     fig.update_traces(mode='lines+markers', line=dict(color='grey', width=1))

     fig.update_layout(
        yaxis=dict(
        showticklabels=False,  # Hide tick labels
        showgrid=True,  # Hide grid lines
        zeroline=False,  # Hide zero line
        title=None  # Remove axis title
    ),
        #title=f'Dividende en FCFA ',
        title = {'text': "Dividende net", 
                            'font': {'color': 'lightgrey', 'size': 18} },
         xaxis_title='Date',
         yaxis_title= 'Fcfa',
          template='plotly_white',
          plot_bgcolor='rgba(0, 0, 0, 0.1)',  # Plot area background color
        paper_bgcolor='rgba(0, 0, 0, 0.1)' # Overall background color
            )

     # Display t    he plot
     st.plotly_chart(fig, use_container_width=True)
     
     # Add company history
     with st.expander('A Propos', expanded=True):
                
                     # Display description content
                     resume =  df_main[df_main['Ticket'] == selected_company]['Description'].unique()[0]
                     st.markdown(f"""
                        <div class="resume">{resume} </div> """,
                          unsafe_allow_html=True)
with c2 :
        stock_data = filter_data(df_main, box[0], box[1])
        #st.write(stock_data)
        
        fig = px.bar(stock_data, x=stock_data['Date'], y=stock_data['Resultat_net'],
                      title=None,
                 labels={'X': 'X Axis Label', 'Y': 'Y Axis Label'},
                 
                 color = 'Resultat_net'
            )
        
        fig.update_traces(showlegend=False  )
                # Hide the y-axis
        fig.update_layout(
        yaxis=dict(
        showticklabels=False,  # Hide tick labels
        showgrid=True,  # Hide grid lines
        zeroline=False,  # Hide zero line
        title=None  # Remove axis title
    ),    
      #  title=f'Bénéfice net',
       title = {'text': "Bénéfice net", 
                            'font': {'color': 'lightgrey', 'size': 18} },
        xaxis_title='Date',
        yaxis_title='Million Fcfa',
        template='plotly_white',
         plot_bgcolor='rgba(0, 0, 0, 0.1)',  # Plot area background color
        paper_bgcolor='rgba(0, 0, 0, 0.1)' # Overall background color
    )
     # Display the plot
        st.plotly_chart(fig, use_container_width=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

