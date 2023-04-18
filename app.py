import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Maximum of Three Numbers

This app tell you which number is bigger out of the three input given
""")
#Get Input

st.header('User Input')

num1 = st.number_input("1st Number")
num2 = st.number_input("2nd Number")
num3 = st.number_input("3rd Number")
  

st.write(num1)

st.subheader('Max Value is')
if (num1 > num2 and num1 > num3):
    st.write(num1)
elif num2 > num3:
    st.write(num2)
else :
    st.write(num3)
#st.write(prediction)

st.subheader('Thanks for using the app')

