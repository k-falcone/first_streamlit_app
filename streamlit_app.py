import streamlit as sl
import pandas as pd
import requests as rq

# Title
sl.title('My Parents\' New Healthy Diner')

# Breakfast Favorites Section
sl.header('Breakfast Favorites')
sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach, & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado Toast')

# Fruit Smoothie Section
sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick List for Fruit Smoothie
fruits_selected = sl.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
sl.dataframe(fruits_to_show)

# New Section to Display Fruityvice API Response
fruityvice_response = rq.get("https://fruityvice.com/api/fruit/watermelon")
sl.text(fruityvice_response)
