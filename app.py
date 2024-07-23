import streamlit as st 
import random

st.header('업다운게임', divider='rainbow') 
clicked = st.button("게임시작")

n = 0
if clicked :
    n = random.randint(1, 100)
    
st.write(f'n={n}')
st.image('./img/what.png')