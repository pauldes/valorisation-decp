
import streamlit as st

from src import functions

# Page properties
st.set_page_config(
    page_title="Qualité des DECP",
    page_icon="./src/static/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
)

# Functions

@st.cache
def cached__load_dataset():
    return functions.load_audit_results_from_disk()

@st.cache
def cached__get_audit_results_from_url(url):
    return functions.get_audit_results_from_url(url)

@st.cache
def cached__get_audit_results_list(year, month, day):
    return functions.get_audit_results_list()

def get_url():
    sessions = st.server.server.Server.get_current()._session_info_by_id
    session_id_key = list(sessions.keys())[0]
    session = sessions[session_id_key]
    url = session.ws.request.connection.context.address[0]
    return url

day = functions.get_current_day()
month = functions.get_current_month()
year =  functions.get_current_year()

# Sidebar

st.sidebar.markdown("""Cette application propose une analyse de la qualité des DECP.
    """)

audit_results_list = cached__get_audit_results_list(year, month, day)

st.sidebar.subheader("Paramétrage")

selected_source = st.sidebar.selectbox("Source à analyser", ["Source 1", "Source 2"])

sidebar_column_1, sidebar_column_2 = st.sidebar.columns(2)
with sidebar_column_1:
    current_created_at = st.selectbox("Date courante", audit_results_list.keys())
with sidebar_column_2:
    old_created_at = st.selectbox("Date à comparer", audit_results_list.keys())

current_url = audit_results_list.get(current_created_at)
old_url = audit_results_list.get(old_created_at)
current_results = cached__get_audit_results_from_url(current_url)
old_results = cached__get_audit_results_from_url(old_url)

st.sidebar.subheader("Plus d'informations")

# Main page

st.image("./src/static/logo-economie-finances-relance.png", width=300)
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