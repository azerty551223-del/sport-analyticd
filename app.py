
import streamlit as st

st.set_page_config(
    page_title="SPORT ANALYTICS",
    page_icon="⚽",
    layout="wide"
)

st.title("⚽ SPORT ANALYTICS")
st.caption("Football & Tennis | Analyse des vainqueurs")

sport = st.sidebar.selectbox(
    "Choisir ton sport",
    ["Football", "Tennis"]
)

st.sidebar.info("Un seul sport analysé à la fois.")

if sport == "Football":

    st.header("⚽ Analyse Football")
    st.write("Compare deux équipes avant leur rencontre.")

    with st.form("football_form"):
        equipe_a = st.text_input("Équipe à domicile")
        equipe_b = st.text_input("Équipe à l'extérieur")

        date = st.date_input("Date du match")

        envoyer = st.form_submit_button("Analyser le match")

    if envoyer:
        if equipe_a.strip() and equipe_b.strip():
            st.subheader(f"{equipe_a} VS {equipe_b}")
            st.write(f"Date : {date}")

            st.warning(
                "En attente de connexion aux statistiques "
                "réelles des équipes."
            )

            st.write("Les résultats analyseront :")
            st.write("- Forme des deux équipes")
            st.write("- 5 à 10 derniers matchs")
            st.write("- Performances domicile / extérieur")
            st.write("- Confrontations directes")
            st.write("- Buts marqués et encaissés")

            st.info(
                "Aucune probabilité n'est affichée tant "
                "que les données ne sont pas vérifiées."
            )
        else:
            st.error("Entre les deux noms des équipes.")

elif sport == "Tennis":

    st.header("🎾 Analyse Tennis")
    st.write("Compare deux joueurs avant leur rencontre.")

    with st.form("tennis_form"):
        joueur_a = st.text_input("Joueur A")
        joueur_b = st.text_input("Joueur B")

        surface = st.selectbox(
            "Surface",
            ["Dur", "Terre battue", "Gazon", "Indoor"]
        )

        envoyer = st.form_submit_button("Analyser le match")

    if envoyer:
        if joueur_a.strip() and joueur_b.strip():
            st.subheader(f"{joueur_a} VS {joueur_b}")
            st.write(f"Surface : {surface}")

            st.warning(
                "En attente de connexion aux statistiques "
                "réelles des joueurs."
            )

            st.write("Les résultats analyseront :")
            st.write("- 10 derniers matchs")
            st.write("- Performances sur la surface")
            st.write("- Confrontations directes")
            st.write("- Pourcentage de victoires")
            st.write("- Statistiques de service et de retour")

            st.info(
                "Aucune probabilité n'est affichée tant "
                "que les données ne sont pas vérifiées."
            )
        else:
            st.error("Entre les deux noms des joueurs.")

st.divider()
st.caption("SPORT ANALYTICS | Version 2.0")
