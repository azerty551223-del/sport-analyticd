
import streamlit as st

st.set_page_config(
    page_title="SPORT ANALYTICS",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ SPORT ANALYTICS")
st.subheader("Football et Tennis")

st.write("Bienvenue sur ton espace d'analyse sportive.")

sport = st.selectbox(
    "Quel sport veux-tu analyser ?",
    ["Football", "Tennis"]
)

if sport == "Football":
    st.header("⚽ Analyse Football")
    st.write("Les statistiques des équipes arriveront ici.")
    
    analyse = st.selectbox(
        "Type d'analyse",
        ["Plus de 1,5 but en première mi-temps",
         "Plus de 2,5 buts",
         "Les deux équipes marquent",
         "Vainqueur du match"]
    )

elif sport == "Tennis":
    st.header("🎾 Analyse Tennis")
    st.write("Les statistiques des joueurs arriveront ici.")
    
    analyse = st.selectbox(
        "Type d'analyse",
        ["Vainqueur du match",
         "Nombre d'aces",
         "Nombre de jeux",
         "Nombre de sets"]
    )

st.divider()
st.caption("SPORT ANALYTICS - Version 1.0")
