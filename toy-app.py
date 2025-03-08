import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("**Diabetes Data**")
db = datasets.load_diabetes()
df = pd.DataFrame(db.data, columns=db.feature_names)

# 显示数据表
st.dataframe(df, use_container_width=True)

# **新增：绘制年龄分布的直方图**
fig, ax = plt.subplots(figsize=(6, 3))
df['age'].hist(bins=10, ax=ax)
fig.suptitle("Age Distribution")
st.pyplot(fig)

# Set page config
apptitle = 'DSSI Toy App'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('My First Streamlit Application')
st.write('Reference: https://docs.streamlit.io/en/stable/api.html#display-data')
st.balloons() 

# Load diabetes dataset
st.subheader('**Diabetes Data**')
db = datasets.load_diabetes()

df = pd.DataFrame(db.data, columns=db.feature_names)

col1, col2 = st.columns([2,1])
with col1:
    # Display dataframe as an interactive table
    st.dataframe(df, use_container_width=True)
with col2:
    # Plot histogram for age of patients
    fig, ax = plt.subplots(figsize=(6, 3))
    if 1==0: # Evaluate True to show plot
        df['age'].hist(bins = 10, ax=ax)
        fig.suptitle("Age Distribution")
        st.pyplot(fig)
