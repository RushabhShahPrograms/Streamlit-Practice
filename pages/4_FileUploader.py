import streamlit as st

st.title("Uploading File")
st.markdown("---")

images = st.file_uploader("Please upload your documents",type=['png','jpg','mp4','mkv','csv','pdf','docs'],accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)
