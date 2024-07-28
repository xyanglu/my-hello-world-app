import streamlit as st
import pandas as pd
import numpy as np

st.title("Yang's Streamlit")

with st.sidebar:
    st.header("About")
    st.write("This is Yang's streamlit app!")

col1, col2 = st.columns(2)

with col1:
    x = st.slider('Choose an x value',1,10)

with col2:
    st.write('The value of ***x*** is',x) 

st.subheader("Chart Visualization")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Blue1", "Blue2", "Orange"])
st.area_chart(chart_data)
