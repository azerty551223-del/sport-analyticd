
import streamlit as st

st.set_page_config(
    page_title="SPORT ANALYTICS",
    page_icon="⚽",
    layout="wide"
)

st.title("SPORT ANALYTICS")
st.caption("Football & Tennis | Analyse statistique")

st.sidebar.title("Navigation")

sport = st.sidebar.selectbox(
    "Choisir un sport",
    ["Accueil", "Football", "Tennis"]
)

if sport == "Accueil":
    st.header("Bienvenue sur SPORT ANALYTICS")
    st.write("Ton espace d'analyse sportive.")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚽ Football")
        st.write("Analyse des buts, des équipes et des performances.")

    with col2:
        st.subheader("🎾 Tennis")
        st.write("Analyse des joueurs, des sets et des statistiques.")

elif sport == "Football":
    st.header("⚽ Analyse Football")
    st.info("Module football en préparation.")
    st.write("Prochainement : buts, forme, statistiques et probabilités.")

elif sport == "Tennis":
    st.header("🎾 Analyse Tennis")
    st.info("Module tennis en préparation.")
    st.write("Prochainement : victoires, aces, jeux et statistiques.")

st.divider()
st.caption("Les analyses seront basées sur des données vérifiables.")
# sport-analyticd
Site gratuit d'analyse statistique de football et de tennis
