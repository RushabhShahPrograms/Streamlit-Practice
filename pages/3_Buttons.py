import streamlit as st

#checkbox
def change():
    st.write("Changed")
    st.write(st.session_state.checker)
state = st.checkbox("Checkbox",value=True,on_change=change,key="checker")
if state:
    st.write("Hi")
else:
    pass

radio_btn = st.radio("In which country do you live?",options=("US","INDIA","UK","CANADA"))
st.write(radio_btn)

def btn_click():
    print("Button clicked")

btn = st.button("Click me!",on_click=btn_click)

select = st.selectbox("What is your favourite car?",options=("Audi","BMW","Ferrari"))

multi_select = st.multiselect("What is your favourite car?",options=("Audi","BMW","Ferrari","Lotus","Lambo"))
st.write(multi_select)