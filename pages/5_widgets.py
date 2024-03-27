import streamlit as st
import time as ts
from datetime import time


st.set_page_config(
    page_title="Widgets",
    page_icon="☸️",
)


st.slider("This is a slider",max_value=1000,min_value=150,value=180)

def converter(value):
    m,s,ms = value.split(":")
    t_s = int(m)*60 + int(s) + int(ms)/1000
    return t_s


val = st.text_area(label="Enter your course title",max_chars=60)
val1 = st.date_input("Enter your registertion date")
val2 = st.time_input("Set your time",value=time(0,0,0))
if str(val) == '00:00:00':
    st.write("Please sent timer")
else:
    sec = converter(str(val2))
    bar = st.progress(0)
    per = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.sleep(per)