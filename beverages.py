from functions import load_csv, clean_price, save_csv, add_date
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Funktion, die dann in "main.py" importiert wird
def show_beverages():
    st.title("Getränkeangebot der Deutschen Bahn")
    st.header("Diese Seite ist aktuell in Bearbeitung, hierier findest du zukünftig Informationen zum historischen und aktuellen Getränkeangebot der Deutschen Bahn")
