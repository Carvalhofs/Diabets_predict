import streamlit as st

st.title("Diabets prediction")

with st.form("features"):
    numero_gravidez = st.number_input("Quantas vezes você já engravidou?", min_value = 0, value = 0)
    glicose = st.number_input ("Quantos ppm de Glicose foi reportado no último exame de sangue?", value = 0)
    pressao_sangue = st.number_input ("Qual a sua pressão sanguínea no último exame realizado?", value = 0)  
    gordura_triceps = st.number_input ("Qual a espessura da gordura localizada no tríceps em milímetros?", value = 0)
    insulina = st.number_input ("Quantos ppm de Insulina foi reportado no último exame de sangue?", value = 0)
    ind_mass_corp = st.number_input ("Qual o seu índice de massa corporal?", value = 0)
    fat_pred_diab = st.number_input ("Qual o seu fator de predisposição à diabetes?", value = 0.0, format = "%f")
    idade = st.number_input ("Qual a sua idade nesse momento?")
    
    enviar = st.form_submit_button("Enviar")




