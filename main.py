import streamlit as st

st.title("Diabets prediction")

with st.form("features"):
    numero_gravidez = st.number_input("Quantas vezes você já engravidou? (Caso nenhuma colocar zero '0')", min_value = 0, value = 0)
    st.form_submit_button("Enviar")
