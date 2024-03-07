import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('https://raw.githubusercontent.com/BraiNeu-F/dicoding_project_polution_in_guanyuan_area/main/data/guanyuan_data_clean.csv', sep=',')


min_date = df['year'].min()
max_date = df['year'].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://images.creativemarket.com/0.1.0/ps/6713806/3500/2330/m1/fpnw/wm0/logos-21-77-.jpg?1563702063&s=c25446499054f94d550e28c39b63e932")
    
    # Mengambil start_year & end_year
    min_year = min_date  
    max_year = max_date  
    start_year = st.selectbox(
        label='Pilih Tahun',
        options=range(min_year, max_year+1),
        index=0
    )

st.header('Polution in Guanyuan Area')

# Grafik 1
st.subheader("Total of CO per Month in 5 years")

plt.figure(figsize=(10,6))

sns.barplot(x='month', y='CO', data=df, hue='year')

plt.xlabel("Month")
plt.ylabel("Total CO")
plt.title("Total of CO per Month")

st.pyplot(plt)

# Grafik 2
st.subheader("Total of Polution in PM2.5 per Month in 5 years")

plt.figure(figsize=(10,6))

sns.barplot(x='month', y='PM2.5', data=df, hue='year')

plt.xlabel("Month")
plt.ylabel("Total PM2.5")
plt.title("Total of PM2.5 per Month")

st.pyplot(plt)
