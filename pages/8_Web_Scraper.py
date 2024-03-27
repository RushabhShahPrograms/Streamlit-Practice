import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(
    page_title="Scraper",
    page_icon="🪛",
    layout="wide"
)


st.markdown("<h1 style='text-align:center;'>Web Scraper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your Keyword")
    search = st.form_submit_button("Search")

if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_="ripi6")
    
    col1, col2 = st.columns(2)  # Move this line here

    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img = figures[i].find("div", class_="MorZF")
            anchor = figures[i].find("a",class_="rEAWd")
            # print(anchor["href"])
            srcset = img.find("img")["srcset"]
            srcset_parts = srcset.split(',')
            image_url = srcset_parts[0].split('?')[0]
            if i == 0:
                col1.image(image_url)
                btn = col1.button("Download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])

            else:
                col2.image(image_url)
                btn = col2.button("Download",key=str(index)+str(i))
                if btn:
                    webbrowser.open_new_tab("https://unsplash.com"+anchor["href"])