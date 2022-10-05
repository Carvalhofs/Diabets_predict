import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from st_on_hover_tabs import on_hover_tabs

with st.sidebar:
        tabs = on_hover_tabs(tabName=['Diagnóstico', 'Vídeo informativo', 'Contatos especialistas'], 
                             iconName=['dashboard', 'money', 'economy'],
                             styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

st.title("Diabets prediction")
st.write("""#### Aplicação busca proporcionar autodiagnóstico preliminar do usuário visando a procura imediata de um médico para diagnóstico precoce de Diabetes.""")

open_modal = st.button("Realizar teste preliminar agora!")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        components.iframe('https://carvalhofs-diabets-predict-model-if4iuc.streamlitapp.com/', width = size, height = 600) 
        
