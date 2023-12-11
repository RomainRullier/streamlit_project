import pandas as pd
import streamlit as st


st.set_page_config(page_title="Streamlit App", page_icon="🧊", layout="wide")

st.title("My first app")

st.markdown("""
  # Titre
  ## Sous-titre
  
    print("Hello world!")
  

""")

#sous-titre
st.subheader("Sous-titre")

#Afficher des éléments sur la page
st.write("Hello world!")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

st.write(df)

#Afficher un graphique
st.line_chart(df)

#Graphique avec Matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x**2)
st.pyplot(fig)

#Afficher une carte
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [48.86, 2.34],
    columns=['lat', 'lon'])

st.map(df)

#Afficher des widgets
st.sidebar.header("Sidebar")
st.sidebar.slider("Slider", 0, 100, 50)
st.sidebar.selectbox("Selectbox", [1, 2, 3])
st.sidebar.multiselect("Multiselect", [1, 2, 3])
st.sidebar.button("Button")

#Afficher un graphique interactif avec Plotly
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
st.plotly_chart(fig)

#Afficher une vidéo
st.video("https://www.youtube.com/watch?v=9JpdAg6uMXs")

#Création de colonnes
col1, col2 = st.columns(2)

with col1:
    x = np.arange(10)
    fig, ax = plt.subplots()
    ax.plot(x, x**2)
    st.pyplot(fig)

with col2:
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    st.plotly_chart(fig)

#Création d'onglets
tabs = ["Tab 1", "Tab 2"]
selected_tab = st.radio("Tabs", tabs)
if selected_tab == "Tab 1":
    st.write("Tab 1")
elif selected_tab == "Tab 2":
    st.write("Tab 2")

