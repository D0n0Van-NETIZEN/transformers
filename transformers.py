import streamlit as pd
import numpy as np 
import pandas as pd

transformers_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(transformers_data)
st.header("Data Description")

myname = st.text_input('name :')
if st.button('Search'):
  st.write(f"search name : {myname}")