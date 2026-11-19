import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    # sep=None aur on_bad_lines="skip" se CSV ka ParserError nahi aayega
    df = pd.read_csv("EURPE ALL.csv", encoding="latin1", sep=None, engine="python", on_bad_lines="skip")
    return df

df = load_data()

st.sidebar.header("Filter Options")

# Pehle column (chahe uska naam 'City' ho ya kuch aur) se Country extract karein
first_col = df.columns[0]
if "Country" not in df.columns:
    df["Country"] = df[first_col].apply(lambda x: x.split(",")[-1].strip() if "," in str(x) else "Unknown")

countries = st.sidebar.multiselect(
    "Country chunein:",
    options=sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())[:5]  # Default pehle 5 countries
)

# Filter lagakar data screen par dikhayein
filtered_df = df[df["Country"].isin(countries)]
st.write(filtered_df)