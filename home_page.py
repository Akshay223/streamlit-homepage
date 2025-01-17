# -*- coding: utf-8 -*-  # Added encoding declaration

import streamlit as st

# Streamlit App Code
st.title("Welcome to My Streamlit App")

# Text input to get user's name
name = st.text_input("Enter your name:")

# Display greeting if name is entered
if name:
    st.write(f"Hello, {name}!")
