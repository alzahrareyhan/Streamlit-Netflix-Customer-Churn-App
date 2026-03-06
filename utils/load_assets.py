import pickle
import streamlit as st
@st.cache_data
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_scalers():
    with open("scalers.pkl", "rb") as f:
        return pickle.load(f)

@st.cache_data
def load_encoders():
    with open("encoders.pkl", "rb") as f:
        return pickle.load(f)