
import streamlit as st

import functions

# Page properties
st.set_page_config(
    page_title="Qualité des DECP",
    page_icon="./src/static/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
)

# Functions

@st.cache
def load_dataset():
    return functions.load_audit_results_from_disk()

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
# total_rows = dataset.shape[0]

st.sidebar.subheader("Paramétrage")

# sources = dataset["source"].unique()
# percent_rows = st.sidebar.slider("Pourcentage de lignes chargées", min_value=10, max_value=100, format="%d")
selected_source = st.sidebar.selectbox("Source à analyser", ["Source 1", "Source 2"])
# selected_num_rows = int(total_rows * percent_rows / 100)
# dataset = dataset.sample(selected_num_rows)
# dataset = dataset[dataset.source==selected_source]

#st.sidebar.subheader("Evolution historique")
sidebar_column_1, sidebar_column_2 = st.sidebar.columns(2)
with sidebar_column_1:
    compare_with_n = st.number_input("Nombre de périodes", min_value=1, step=1)
with sidebar_column_2:
    compare_with_element = st.radio("Type de période", ["Année", "Mois", "Jour"])

st.sidebar.subheader("Plus d'informations")

# Main page

st.image("./src/static/logo-economie-finances-relance.png", width=150)
st.title("Qualité des Données Essentielles de la Commande Publique (DECP)")

st.text(f"Source : {selected_source}")

kpi_container = st.container()
kpi_container.subheader("Synthèse")
kpi_col_1, kpi_col_2, kpi_col_3, kpi_col_4, kpi_col_5, kpi_col_6, kpi_col_7  = kpi_container.columns([2, 1, 1, 1, 1, 1, 1])
kpi_col_1.metric("Qualité globale", "A+", "C")
kpi_col_1.markdown(f"*Rang source:* **{1}**")
kpi_col_2.metric("Validité", "12%", "8%")
kpi_col_2.markdown(f"*Rang:* **{3}**")
kpi_col_3.metric("Complétude", 42, 2)
kpi_col_3.markdown(f"*Rang:* **{2}**")
kpi_col_4.metric("Conformité", 42, 2, delta_color="off")
kpi_col_4.markdown(f"*Rang:* **{5}**")
kpi_col_5.metric("Cohérence", 42, 2)
kpi_col_5.markdown(f"*Rang:* **{4}**")
kpi_col_6.metric("Singularité", 42, 2)
kpi_col_6.markdown(f"*Rang:* **{2}**")
kpi_col_7.metric("Exactitude", 42, 2)
kpi_col_7.markdown(f"*Rang:* **{1}**")

details_container = st.container()
details_container.subheader("Détails des indicateurs")
details_col_1, details_col_2, details_col_3 = details_container.columns(3)

singularite_container = details_col_1.container()
singularite_container.markdown("**Singularité**")
singularite_container.info(f"""
    **{42}** identifiants non uniques
    \n\n
    **{42}** lignes dupliquées
    """)

validite_container = details_col_1.container()
validite_container.markdown("**Validité**")
validite_container.info(f"""
    **{42}** jours depuis la dernière publication
    \n\n
    **{42}** écart moyen entre notification et publication
    """)

completude_container = details_col_2.container()
completude_container.markdown("**Complétude**")
completude_container.info(f"""
    **{42}** données manquantes
    \n\n
    **{42}** valeurs non renseignées
    """)

conformite_container = details_col_2.container()
conformite_container.markdown("**Conformité**")
conformite_container.info(f"""
    **{42}** caractères mal encodés ou illisibles
    \n\n
    **{42}** formats ou valeurs invalides
    """)

exactitude_container = details_col_3.container()
exactitude_container.markdown("**Exactitude**")
exactitude_container.info(f"""
    **{42}** valeurs aberrantes
    \n\n
    **{42}** valeurs extrêmes
    """)

coherence_container = details_col_3.container()
coherence_container.markdown("**Cohérence**")
coherence_container.info(f"""
    **{42}** incohérences temporelles
    \n\n
    **{42}** incohérences montant/durée
    """)