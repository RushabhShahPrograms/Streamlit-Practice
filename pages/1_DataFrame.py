import streamlit as st

st.set_page_config(
    page_title="DataFrames",
    page_icon="🐼",
)


#pandas and Data
import pandas as pd
table = pd.DataFrame({"Column 1":[1,6,3,5,4,2,7],"Coumn 2":[11,12,13,14,15,16,17]})
st.table(table)
st.dataframe(table)