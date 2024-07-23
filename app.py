import streamlit as st 
import random
import time

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