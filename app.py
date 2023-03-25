import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt





st.title('タイトル')
st.header('ここはヘッダー')
st.subheader('サブヘッダーをつけてみる')

col1,col2 = st.columns(2)

with col1:
    st.text('テキストはここからはじまるよ。長い文章は,バックスラッシュ+nで\nで改行することが出来るよ。')

    code = '''
    iimport streamlit as st

    st.title('タイトル')
    st.header('ここはヘッダー')
    st.subheader('サブヘッダーをつけてみる')
    '''
    st.code(code,language ='python')

    image = Image.open('pika.jpg')
    st.image(image,width=200)

    today = st.date_input(
        '今日の日付',
        datetime.date(2023,3,25))


    with st.form(key="profile_form"):
        name = st.text_input('お名前')
        school = st.text_input('学校')
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ{school}の{name}さん！')


with col2:

    df = pd.read_csv('data.csv',index_col='月')
    st.dataframe(df)

    st.line_chart(df)
    st.bar_chart(df['最高気温(℃)'])

fig, ax = plt.subplots()
ax.plot(df.index,df['最高気温(℃)'])
ax.set_title('maximum temperature')
st.pyplot(fig)

