import requests
import json
import streamlit as st

st.title(" ☕☕ List of coffees ☕☕ ")
type_of_coffee = st.selectbox("type?",["hot","iced"])
filter = st.text_input("filter?")

if type_of_coffee:
    url = "https://api.sampleapis.com/coffee/" + type_of_coffee + "/?title_like=" + filter
    response = requests.get(url)
    coffees =  json.loads(response.content)
    #st.table(coffees)
    for coffee in coffees:
        st.text(coffee["title"])
        st.image(coffee["image"])

