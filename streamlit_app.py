import streamlit
import pandas
import snowflake.connector
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')
myfruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruit_list=myfruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits",list(myfruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruits",list(myfruit_list.index),['Avocado','Strawberries'])
fruits_to_show=myfruit_list.loc[fruits_selected]
streamlit.dataframe(myfruit_list)
