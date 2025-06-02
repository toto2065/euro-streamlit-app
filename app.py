import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="UEFA EURO Analysis", layout="wide")
st.title("⚽ UEFA EURO Tournament Analysis")

st.markdown("""
This app presents an analysis of UEFA EURO tournament data, including goals, red cards, attendance, and match averages.
""")

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1N_KA0v890rH6nnou01MRHvWo3zknWDoK"
    return pd.read_csv(url)

df = load_data()

if st.checkbox("Show Raw Data"):
    st.dataframe(df)

years = st.slider("Select Year Range", 
                  int(df['year'].min()), 
                  int(df['year'].max()), 
                  (int(df['year'].min()), int(df['year'].max())))
filtered_df = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]

st.subheader("⚽ Distribution of Total Goals")
fig1, ax1 = plt.subplots()
sns.histplot(data=filtered_df, x='goals', kde=True, ax=ax1)
st.pyplot(fig1)

st.subheader("🟥 Distribution of Total Red Cards")
fig2, ax2 = plt.subplots()
sns.histplot(data=filtered_df, x='red_cards', kde=True, ax=ax2)
st.pyplot(fig2)

st.subheader("👥 Distribution of Tournament Attendance")
fig3, ax3 = plt.subplots()
sns.histplot(data=filtered_df, x='attendance', kde=True, ax=ax3)
st.pyplot(fig3)

st.subheader("⚽ Average Goals per Match")
fig4, ax4 = plt.subplots()
sns.histplot(data=filtered_df, x='goals_avg', kde=True, ax=ax4)
st.pyplot(fig4)

st.subheader("🟥 Average Red Cards per Match")
fig5, ax5 = plt.subplots()
sns.histplot(data=filtered_df, x='red_cards_avg', kde=True, ax=ax5)
st.pyplot(fig5)
