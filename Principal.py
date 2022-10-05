import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from st_on_hover_tabs import on_hover_tabs

st.title("Diagnóstico preliminar - Diabetes")
st.write("""#### Clique no botão abaixo para preencher informações necessárias para o diagnóstico.""")

open_modal = st.button("Realizar teste preliminar agora!")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        components.iframe('https://carvalhofs-diabets-predict-model-model-hi8fmn.streamlitapp.com/', width = size, height = 600) 
        
