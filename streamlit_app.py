import streamlit as st
import pandas as pd

st.title('My Streamlit App')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)



