import streamlit as st 
import pandas as pd


st.subheader('Uploading the csv file')
df=st.file_uploader('Upload the csv file: ',type=['csv','xls'])      #uploading

st.subheader('Loading the csv file')
df=pd.read_csv('/Users/ginnyshai/Desktop/lib/streamlit/Sales.csv')
st.table(df)

if df is not None:
    st.table(df.head())


######################
st.subheader('Dealing with Images')
st.subheader('Uploading with Images')
img=st.file_uploader('Upload the Image: ',type=['png','jpg','jpeg']) # uploading 
if img is not None:
    st.image(img)
st.subheader('Loading with Images')
st.image('/Users/ginnyshai/Desktop/lib/streamlit/gin.jpeg')           # loading directly


#######################
st.subheader('Wrorking with videos')
video_file= st.file_uploader('Upload the video: ',['mp4','mkv'])

if video_file is not None:
    st.video(video_file)
    
st.video('/Users/ginnyshai/Desktop/lib/streamlit/video.mp4')


########################

st.subheader('Working with Audio')
st.audio('/Users/ginnyshai/Desktop/lib/streamlit/song.mp3')
aud=st.file_uploader('Select the audio: ',type=['mp3'])
if aud is not None:
    st.audio(aud.read())




