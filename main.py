import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components

st.title("Diabets prediction")
st.write("""#### Aplicação busca proporcionar autodiagnóstico preliminar do usuário visando a procura imediata de um médico para diagnóstico precoce de Diabetes.""")

open_modal = st.button("Realizar teste preliminar agora!")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        components.iframe('https://carvalhofs-diabets-predict-model-if4iuc.streamlitapp.com/', width = 500, heigth = 1000) 
        
