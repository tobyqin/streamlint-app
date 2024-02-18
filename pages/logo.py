
from streamlit_extras.app_logo import add_logo
import streamlit as st

# add kitten logo
add_logo("https://placekitten.com/100/100")
add_logo("https://placekitten.com/100/100", height=100)
st.write("👈 Check out the cat in the nav-bar!")