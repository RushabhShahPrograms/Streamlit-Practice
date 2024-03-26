import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)



st.title("Hi! I am streamlit web app")
st.subheader("Hi this is the subheader")
st.header("This is the header")

st.text("This is the text function")

# Markdown function
st.markdown("**Hello** *everyone* this is the markdown")
st.markdown("> This is the quote")
st.markdown("---")
st.markdown("[Google](https://google.com)")
st.markdown("---")

#caption
st.caption("This is caption")

#latex
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

#json
json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)

#code
code = """
print(hello world)
if(happy==True):
    print("I am happy")
"""
st.code(code,language="python")

#swiss army knife
st.write("## H2")
st.metric(label="Wind Speed",value="120ms⁻¹",delta="1.4ms⁻¹")


#removing hamburger
# st.markdown("""
# <style>
# .st-emotion-cache-6q9sum.ef3psqc4
#             {
#             visibility:hidden;
#             }
# </style>
# """,unsafe_allow_html=True)