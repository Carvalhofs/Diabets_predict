import streamlit as st
import streamlit_modal as modal
import streamlit.components.v1 as components
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(page_title='Diagnóstico Diabetes', layout="wide", menu_items=None, initial_sidebar_state = 'collapsed')

st.title("Diagnóstico preliminar - Diabetes")

st.markdown("""<p>O diagnóstico precoce do diabetes é uma ação de prevenção secundária que tem o objetivo de identificar os sinais e sintomas preliminares de uma doença que, segundo o <a href = "https://diabetesatlas.org/", target = "_blank">Atlas Mundial do Diabetes</a>, já atinge mais de 463 milhões de adultos em todo o mundo.

E o que é mais impressionante: de acordo com o levantamento, publicado pela International Diabetes Federation (IDF), metade dessas pessoas sequer sabe que tem a doença!

Isso quer dizer que um em cada dois diabéticos não toma medidas preventivas para evitar complicações de saúde pelo simples fato de ainda não ter sido diagnosticado.

E todos sabemos que, no caso do diabetes, descobrir a doença no seu início é fundamental. Se o paciente souber controlar seu nível de glicose e ter acompanhamento médico, poderá evitar consequências gravíssimas, como infarto, derrame cerebral ou cegueira.</p>""", unsafe_allow_html=True)

st.markdown("""<p>Para mais informações, assista a um video informativo <a href = "https://carvalhofs-diabets-predict-principal-l1e0kt.streamlitapp.com/Video_Informativo", target = "_self">clicando aqui</a></p>""", unsafe_allow_html=True)


st.write("""#### Clique no botão abaixo para realizar o teste diagnóstico.""")

st.markdown('<a href="https://carvalhofs-diabets-predict-model-model-hi8fmn.streamlitapp.com/" target="_self"><button type="button">Realizar teste agora!</button></a>', unsafe_allow_html=True)