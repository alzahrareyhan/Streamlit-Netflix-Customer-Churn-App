import streamlit as st
from views.tentang_project import show_tentang_project
from views.tentang_saya import show_tentang_saya
from views.prediction import show_prediction
from views.kontak import show_kontak

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Netflix Customer Churn App",
    page_icon="📉",
    layout="wide"
)

# ------------------- Load CSS -------------------
with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------- Sidebar -------------------
st.sidebar.markdown(
    "<div class='card'><div class='h1'>📉 Churn App</div>"
    "<p class='muted'>Netflix Customer Churn</p></div>",
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "Menu",
    ["Tentang Saya", "Tentang Project", "Prediction", "Kontak"],
    index=2
)

if menu == "Tentang Saya":
    show_tentang_saya()
elif menu == "Tentang Project":
    show_tentang_project()
elif menu == "Prediction":
    show_prediction()
else:
    show_kontak()