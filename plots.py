import streamlit as st 
import  pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

st.header('1. Charts with random number')
chart_data=pd.DataFrame(np.random.randn(20,3), columns=['Line-1','Line-2','Line-3'])

st.subheader('Line Charts')
st.line_chart(chart_data)

st.subheader('Area Charts')
st.area_chart(chart_data)

st.subheader('Bar Charts')
st.bar_chart(chart_data)

st.header('2. Data Visualisation with matplotlib and seaborn')

st.subheader('Loading the data frame')
df=pd.read_csv('/Users/ginnyshai/Desktop/lib/streamlit/iris.csv')
st.dataframe(df)


st.subheader('Bar graph with matplotlib')
fig=plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('Distribution plot with seaborn')
fig1=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig1)

st.header('3. Multiple Graph in one column')
col1,col2= st.columns(2)
with col1:
    col1.header ='KDE=False'
    fig11=plt.figure(figsize=(11,5))
    sns.distplot(df['sepal_length'],kde=False)         # KDE shows line on graph
    st.pyplot(fig11)

with col2:
    col2.header ='Hist=False'
    fig12=plt.figure(figsize=(11,5))
    sns.distplot(df['sepal_length'],hist=False)         # KDE shows line on graph
    st.pyplot(fig12)
    

st.header('4. Changing Style')

col1, col2=st.columns(2)
with col1:
    fig13=plt.figure(figsize=(5,5))
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig13)
    
with col2:
    fig14=plt.figure(figsize=(5,5))
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['petal_length'],hist=False)
    st.pyplot(fig14)
    

st.header('5. Exploring different Graphs')
st.subheader('5.1 Scatter plot')
fig,ax=plt.subplots(figsize=(8,5))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('5.2 count plot')
fig=plt.figure(figsize=(8,5))
sns.countplot(data=df, x='species')
st.pyplot(fig)

st.subheader('5.3 Box plot')
fig=plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='species',y='petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin plot')
fig=plt.figure(figsize=(8,5))
sns.violinplot(data=df, x='species',y='petal_length')
st.pyplot(fig)

