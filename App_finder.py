#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd

# Load the merged dataset
merged_df = pd.read_csv('/Users/tanishqbakliwal/Desktop/merged_data.csv')  

# Convert 'brand' column to strings
merged_df['brand'] = merged_df['brand'].astype(str)

# Set page title
st.set_page_config(page_title="Winery")

# Display application name and tagline in cursive font
st.markdown(
    """
    <div style="background-color:#f63366;padding:10px;border-radius:10px">
        <h1 style="font-family:cursive;color:white;text-align:center;">Winery</h1>
        <h2 style="font-family:cursive;color:white;text-align:right;font-size:18px;">~Time To Wine Down</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar title and description
st.sidebar.title("Wine Finder")
st.sidebar.write("Find the right wine for you!")

# Sidebar filters
selected_brand = st.sidebar.selectbox("Select Brand", sorted(merged_df['brand'].unique()))
min_rating = st.sidebar.slider("Minimum Rating", min_value=0, max_value=5, value=0, step=1)

# Filter the dataset based on user inputs
filtered_df = merged_df[(merged_df['brand'] == selected_brand) & (merged_df['reviews.rating'] >= min_rating)]

# Display the filtered dataset
st.write("Filtered Wine List:")
st.write(filtered_df)




