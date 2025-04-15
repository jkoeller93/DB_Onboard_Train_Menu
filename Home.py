from functions import load_csv, clean_price, save_csv, add_date
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Funktion, die dann in "main.py" importiert wird
def show_home():
    folder = r"C:\Köllermeier\10_Data_Science_Weiterbildung\Hausaufgaben\Projekte\DB_Speisekarte"
    csv = "food_all_cleaned"
    df = pd.read_csv(f"{folder}\\{csv}.csv")    # DataFrame erstellen und einlesen aus csv

    st.title("Bordgastronomie der Deutschen Bahn")
    st.write("Auf dieser Seit findest du allgemeine Informationen und Statistiken zum Speise- und Getränkeangebot der Deutschen Bahn.")
    st.write("Navigiere gerne über die Reiter oben in der Leiste, um Informationen zu den Speisen und Getränken zu erhalten.")

    st.divider()
    st.header(f"Allgemeine Statistiken zum gastronomischen Angebot seit {df["date"].min()}:")

    df_statistics = pd.DataFrame(
        {
            "Produkte gesamt": [df["name"].nunique(), "tbd"],
            "Produkte aktuell": [df[df["date"] == df["date"].max()]["name"].nunique(), "tbd"],
            "Anzahl Kategorien": [df["category"].nunique(), "tbd"],
            "Vegane Produkte": [df[df["vegan"] == "Vegan"]["name"].nunique(), "tbd"],
            "Vegetarische Produkte": [df[df["vegetaric"] == "Vegetarisch"]["name"].nunique(), "tbd"],
            "Bio-Produkte": [df[df["bio"] == "Bio"]["name"].nunique(), "tbd"]
        },
    index = ["Speisen", "Getränke"]
    )
    st.write(df_statistics)

    st.markdown(
        '<a href="https://db-bordgastronomie.de/digitalespeisekarte" target="_blank">Klicke HIER um zur aktuellen Speisekarte zu gelangen</a>',
        unsafe_allow_html=True
    )

