import streamlit as st 
import random
import time
import pandas as pd

# 데이터 프레임을 session state로 처리
if 'df' not in st.session_state :
   st.session_state.df = pd.read_excel('./성적계산.xlsx')

st.header('성적계산', divider='rainbow') 
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   bt1 = st.button('성적계산')

with col2:
   bt2 = st.button('순위계산')

with col3:
   bt3 = st.button('학점계산') 

with col4:
   bt4 = st.button('파일저장') 

with col5:
   bt5 = st.button('성적현황') 

# 데이터 전처리
st.session_state.df.fillna(0, inplace=True)
st.session_state.df['학번'] = st.session_state.df['학번'].astype(str).str.replace(',','')

st.dataframe(st.session_state.df)