import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from st_on_hover_tabs import on_hover_tabs

with st.sidebar:
        tabs = on_hover_tabs(tabName=['Diagnóstico preliminar', 'Vídeo informativo', 'Contatos especialistas'], 
                             iconName=['Diagnóstico preliminar', 'Vídeo informativo', 'Contatos especialistas'],
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
    if tabs =='Diagnóstico preliminar':
        components.iframe('https://carvalhofs-diabets-predict-main-h9ch0x.streamlitapp.com/')

    elif tabs == 'Vídeo informativo':
        <iframe width="853" height="480" src="https://www.youtube.com/embed/aErKsc2D8qQ" title="Você sabe o que é Diabetes?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    elif tabs == 'Contatos especialistas':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))

st.title("Diagnóstico preliminar - Diabetes")
st.write("""#### Clique no botão abaixo para preencher informações necessárias para o diagnóstico.""")

open_modal = st.button("Realizar teste preliminar agora!")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        components.iframe('https://carvalhofs-diabets-predict-model-if4iuc.streamlitapp.com/', width = size, height = 600) 
        
