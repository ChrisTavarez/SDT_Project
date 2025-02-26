import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px




st.header('Market of Used Vehicles')
st.write('Filter the data below by Car Make & Model')

vehicles = pd.read_csv('vehicles_us.csv')

vehicles['date_posted'] = pd.to_datetime(vehicles['date_posted'])

vehicles['bool_column'] = vehicles['is_4wd'].fillna(0).astype(bool)

vehicles['model_year'] = vehicles.groupby('model')['model_year'].transform(lambda x: x.fillna(x.mean())) 


vehicles["model_year"] = vehicles["model_year"].astype(str).str.replace(",", "").astype(float).astype(int)







Car_Choice = vehicles['model'].unique()

Make_Model = st.selectbox('Select A Car', Car_Choice)

min_year, max_year = vehicles['model_year'].min(), vehicles['model_year'].max()

year_range = st.slider("Choose years", value=(min_year, max_year), min_value=min_year,max_value= max_year)

actual_range = list(range(year_range[0], year_range[1]+1))

vehicles_filtered = vehicles[ (vehicles['model'] == Make_Model) & (vehicles['model_year'].isin(list(actual_range)) )]

vehicles_filtered




st.header('Price Analysis')

st.write('Lets create distributions that allow us to see the prices of the vehicles, based on different aspects of the cars')

list_for_hist = ['cylinders','fuel','transmission','type']

selected_type = st.selectbox('Split for Price Distribution', list_for_hist)

fig_1 = px.histogram(vehicles, x='price', color = selected_type)
fig_1.update_layout(title= "<b> Split of price by {}</b>".format(selected_type))
st.plotly_chart(fig_1)





