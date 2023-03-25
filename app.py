import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import webbrowser







st.title('真岡市の魅力')


st.header('ＳＬの町')
st.subheader('着ていくものは何がいい？')
st.text('過去5年の平均気温を見てみると、決して高くは\nないけど、最高気温は2018年で30℃、去年は28.8\n℃になっているんだね。')

  
image = Image.open('pika.jpg')
st.image(image,width=200)
    

st.text("真岡市 4月の平均気温")
df = pd.read_csv('moka.csv',index_col='年')
st.dataframe(df)
image = Image.open('mouka.png')
st.image(image,width=300)



st.header('おすすめグルメ')
col1,col2 = st.columns(2)
with col1:
    st.text("道の駅 にしのみや")
    image = Image.open('nisinomiya.jpg')
    st.image(image,width=300)
    image = Image.open('nisinomiya2.jpg')
    st.image(image,width=300)
with col2: 
    st.text("宇都宮 みんみん")
    image = Image.open('minmin.jpg')
    st.image(image,width=300)
    image = Image.open('minmin2.jpg')
    st.image(image,width=300)

submit_btn = st.button('真岡をもっと詳しく')

if submit_btn : 
    webbrowser.open('https://www.city.moka.lg.jp/citypromotion/about_moka/7644.html')

