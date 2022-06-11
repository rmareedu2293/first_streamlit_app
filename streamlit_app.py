import streamlit
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')

import pandas
myfruit_list=pandas.read_csv("https:/uni-lab-files.s3.us.west-2.amazonaws.com/dadw/fruit_macros.txt")
streamlit.dataframe(myfruit_list)
