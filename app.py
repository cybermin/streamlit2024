import streamlit as st 
import random

st.header('주사위게임', divider='rainbow') 
clicked = st.button("주사위던지기", type="primary")
if clicked :
    n = random.randint(1,6)
    st.image(f'./img/{n}.png')