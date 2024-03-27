import streamlit as st


st.set_page_config(
    page_title="Charts",
    page_icon="📈",
)



st.sidebar.write("Hello this is my side bar")

st.header("Charts")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
bar_x = np.array([1,2,3,4,5])

# fig = plt.figure()
# plt.plot(x,np.sin(x))
# st.write(fig)


opt = st.sidebar.radio("Select any Graph",options=("Line","Bar","H-Bar"))
if opt == "Line":
    st.markdown("<h1 style='text-align:center;'>Line Chart</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig)

elif opt == "Bar":
    st.markdown("<h1 style='text-align:center;'>Bar Chart</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.bar(bar_x,bar_x*10)
    st.write(fig)

else:
    st.markdown("<h1 style='text-align:center;'>Bar-H Chart</h1>",unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    plt.barh(bar_x*10,bar_x)
    st.write(fig)