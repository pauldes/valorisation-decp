
import streamlit as st

import functions

# Page properties
st.set_page_config(
    page_title="Qualité des DECP",
    page_icon="./src/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
)

st.sidebar.title("Sidebar title")
st.sidebar.markdown(
"""
Sidebar markdown text
"""
)
st.sidebar.text("Sidebar text")
selected_source = st.sidebar.selectbox("Source", ["Source 1", "Source 2"])

st.title("Qualité des Données Essentielles de la Commande Publique (DECP)")
st.header("Header")
st.subheader("Subheader")
st.text(f"Selected source : {selected_source}")

dataset = functions.load_data_from_disk(n_rows=10)
st.text("First 10 rows :")
st.dataframe(dataset)