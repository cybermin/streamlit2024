import streamlit as st 
import random
import time

if 'n' not in st.session_state:
    st.session_state.n = 0

if 'flag' not in st.session_state:
    st.session_state['flag'] = True

st.header('업다운게임', divider='rainbow') 

if st.session_state['flag'] :
    clicked = st.button('게임시작')
    if clicked :
        st.session_state.flag = False
        st.session_state.n = random.randint(1,100)
    st.image('./img/what.png')
else :
    st.subheader('게임중...')
    usern = st.number_input("1에서 100까지 정수를 입력", value=None, placeholder="정수입력")
    if usern.isdigit() :
        usern = int(usern)
        if usern > st.session_state.n : 
            st.image('./img/down.png')
        elif usern < st.session_state.n : 
            st.image('./img/up.png')
        else :
            st.image('./img/good.png')
            st.session_state.flag = True
            st.session_state.n = None
            st.success("정답! 5초 후에 초기화")
            time.sleep(5)
            st.experimental_rerun()