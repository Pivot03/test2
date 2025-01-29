# Day3: Data Visualization Using Streamlit

import streamlit as st


st.title("DON'T TOGGLE THE SWITCH")

on = st.toggle("**Toggle if you are brave...**")


if on:
    st.image("Ghost.jpg")
    st.write("***Boooo!!!  :)***")
   
    
    
    
    
