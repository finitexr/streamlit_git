from matplotlib import pyplot as plt
import streamlit as st 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Used Bikes Data Analysis")
st.header("Data Set")

df = pd.read_csv('Used_Bikes.csv')
data = df.tail(100)
st.write(data)
st.header("Comparing Price with bike specs")

st.text("................................................................................................")
st.subheader("Relation between kms driven and the price")
st.subheader("- The price is inversely proportional to the kms driven :")
sns.lineplot(x='kms_driven',y='price',data=data , marker='*' , color='red',size=15 )
st.pyplot()

st.text("................................................................................................")
st.subheader("Relation between bike age and the price")
st.subheader("- The price is also inversely proportional to the bike age :")
sns.lineplot(x='age',y='price',data=data , marker='o' , color='blue')
st.pyplot()

st.text("................................................................................................")
st.subheader("Relation between bike power and the price")
st.subheader("- The price is directly proportional to the bike power :")
sns.lineplot(x='power',y='price',data=data , marker='o' , color='blue')
st.pyplot()

st.text("................................................................................................")
st.header("BASIC ANALYSIS")
st.subheader("Most Expensive 3 bikes")
data_price = data.groupby('price')
price_max = data_price.max().tail(3)
sns.lineplot(x='bike_name',y='price',data=price_max , marker='o' , color='green')
st.pyplot()

st.subheader("most powerfull 3 bikes")
data_power = data.groupby('power')
power_max = data_power.max().tail(3)
sns.lineplot(x='bike_name',y='power',data=power_max , marker='X' , color='red')
st.pyplot()
