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

def user_input_features():
    num1 = st.number_input("num1")
    num2 = st.number_input("num2")
    num3 = st.number_input("num3")
  
    data = {'1st Number': num1,
            '2nd Number': num2,
            '3rd Number': num3,
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())


st.subheader('Max Value is')
if (num1 > num2 and num1 > num3):
    st.write(num1)
elif num2 > num3:
    st.write(num2)
else :
    st.write(num3)
#st.write(prediction)

st.subheader('Thanks for using the app')

