import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.header("Exploring Data with Streamlit")

# Creating a simple DataFrame
data = pd.DataFrame({
    'A': np.random.rand(100),
    'B': np.random.rand(100)
})

st.subheader("DataFrame")
st.write(data)

st.subheader("Line Chart")
st.line_chart(data)

if st.checkbox("Show DataFrame"):
    st.dataframe(data)

age = st.slider("Choose your age", 0, 100, 25)
st.write(f"You selected: {age} years old")
