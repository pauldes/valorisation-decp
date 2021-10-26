
import streamlit as st

import functions

# Page properties
st.set_page_config(
    page_title="Qualité des DECP",
    page_icon="./src/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
)

# Functions

@st.cache
def load_dataset(n_rows=None):
    return functions.load_data_from_disk(n_rows=n_rows)

def get_url():
    sessions = st.server.server.Server.get_current()._session_info_by_id
    session_id_key = list(sessions.keys())[0]
    session = sessions[session_id_key]
    url = session.ws.request.connection.context.address[0]
    return url

# Sidebar

st.sidebar.markdown("""Cette application propose une analyse de la qualité des DECP.
    """)

dataset = load_dataset()
total_rows = dataset.shape[0]

st.sidebar.subheader("Paramétrage")

sources = dataset["source"].unique()
percent_rows = st.sidebar.slider("Pourcentage de lignes chargées", min_value=10, max_value=100, format="%d")
selected_source = st.sidebar.selectbox("Source à analyser", sources)
selected_num_rows = int(total_rows * percent_rows / 100)
dataset = dataset.sample(selected_num_rows)
dataset = dataset[dataset.source==selected_source]

st.sidebar.subheader("Evolution historique")
sidebar_column_1, sidebar_column_2 = st.sidebar.columns(2)
with sidebar_column_1:
    compare_with_n = st.number_input("Nombre de périodes", min_value=1, step=1)
with sidebar_column_2:
    compare_with_element = st.radio("Type de période", ["Année", "Mois", "Jour"])

st.sidebar.subheader("Plus d'informations")

# Main page

st.title("Qualité des Données Essentielles de la Commande Publique (DECP)")
st.header("Header")
st.subheader("Subheader")
st.text(f"Selected source : {selected_source}")

st.text("First 10 rows :")
st.dataframe(dataset)

st.metric("My metric", 42, 2)

st.text(get_url())