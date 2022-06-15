import streamlit
import pandas
import requests
#import snowflake.connector
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('Hard Boiled Free Range Egg')
myfruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruit_list=myfruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits",list(myfruit_list.index),['Avocado','Strawberries'])
fruits_selected=streamlit.multiselect("Pick some fruits",list(myfruit_list.index),['Avocado','Strawberries'])
fruits_to_show=myfruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
my_cur.execute("SELECT CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row=my_cur.fetchone()
streamlit.text("HThefruit load list contains")
streamlit.text(my_data_row)
