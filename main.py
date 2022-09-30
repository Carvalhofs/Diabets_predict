import streamlit as st

st.title("Diabets prediction")

with st.form("features"):
    numero_gravidez = st.number_input("Quantas vezes você já engravidou?", min_value = 0, value = 0)
    enviar = st.form_submit_button("Enviar")
if enviar:
    st.write(numero_gravidez)