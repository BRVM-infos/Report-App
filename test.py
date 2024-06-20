import streamlit as st
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_icon= "🌍",
    layout="wide", 
    page_title= "BRVM",  
    initial_sidebar_state="expanded")

# Function to get the device type based on the screen width
def get_device_type():
    width = st.sidebar.slider('Screen Width (px)', 300, 2000, 800)
    if width <1200:
        return 'mobile'
    else:
        return 'desktop'

# Determine the device type
device_type = get_device_type()

# Set width and height based on device type
if device_type == 'mobile':
    plot_width, plot_height = 600, 600

else:
    plot_width, plot_height = 800, 600

# Sample data
data = [go.Box(y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]

# Define the layout with custom width and height
layout = go.Layout(
    width=plot_width,
    height=plot_height
)

# Create the figure with the data and layout
fig = go.Figure(data=data, layout=layout)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
