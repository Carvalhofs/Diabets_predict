import streamlit as st

st.title("Diabets prediction")

with st.form("imc"):
    altura = st.number_input ("Qual a sua altura em metros?")
    peso = st.number_input ("Qual o seu peso em Quilos (Kg)?")
    enviar = st.form_submit_button("Enviar")
    if enviar:
        ind_mass_corp = (peso/(altura*altura)).roud(2)
        st.write(f'Seu índice de massa corpórea (IMC) é {ind_mass_corp}')
with st.form("features"):
    numero_gravidez = st.number_input("Quantas vezes você já engravidou?", min_value = 0, value = 0)
    glicose = st.number_input ("Quantos ppm de Glicose foi reportado no último exame de sangue?", value = 0)
    pressao_sangue = st.number_input ("Qual a sua pressão sanguínea no último exame realizado?", value = 0)  
    espessura_pele = st.number_input ("Qual a espessura da dobra subcutanea tricipital em milímetros? (medida realizada com adipometro na regiao do tríceps)", value = 0)
    insulina = st.number_input ("Quantos µIU/mL de Insulina foi reportado no último exame de sangue?", value = 0)
    fat_pred_diab = st.number_input ("Qual o seu fator de predisposição à diabetes? (baseado em histórico familiar)", value = 0.0, format = "%f")
    idade = st.number_input ("Qual a sua idade nesse momento?", value = 0)
    
    enviar = st.form_submit_button("Enviar")




