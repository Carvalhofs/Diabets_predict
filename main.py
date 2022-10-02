import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
st.title("Diabets prediction")

with st.form("features"):
    altura = st.number_input ("Qual a sua altura em metros?")
    peso = st.number_input ("Qual o seu peso em Quilos (Kg)?")
    numero_gravidez = st.number_input("Quantas vezes você já engravidou?", min_value = 0, value = 0)
    glicose = st.number_input ("Quantos mg/dL de Glicose foi reportado no último exame de sangue?", value = 0)
    pressao_sangue = st.number_input ("Qual a sua pressão sanguínea no último exame realizado?", value = 0)  
    espessura_pele = st.number_input ("Qual a espessura da dobra subcutanea tricipital em milímetros? (medida realizada com adipometro na regiao do tríceps)", value = 0)
    insulina = st.number_input ("Quantos µIU/mL de Insulina foi reportado no último exame de sangue?", value = 0)
    fat_pred_diab = st.number_input ("Qual o seu fator de predisposição à diabetes? (baseado em histórico familiar)", value = 0.0, format = "%f")
    idade = st.number_input ("Qual a sua idade nesse momento?", value = 0)
    enviar = st.form_submit_button("Enviar")



def prediction(ind_mass_corp, numero_gravidez, glicose, pressao_sangue,espessura_pele,insulina,fat_pred_diab,idade, model = classifier):  
   
    prediction = model.predict(
        [[ind_mass_corp, numero_gravidez, glicose, pressao_sangue,espessura_pele,insulina,fat_pred_diab,idade]])
    print(prediction)
    return prediction
if enviar:
    ind_mass_corp = (peso/(altura*altura))
    st.write('Seu índice de massa corpórea (IMC) é {:.2f}'.format(ind_mass_corp))
    st.write(prediction(ind_mass_corp, numero_gravidez, glicose, pressao_sangue,espessura_pele,insulina,fat_pred_diab,idade))


