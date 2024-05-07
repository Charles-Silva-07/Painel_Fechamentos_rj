import streamlit as st
import locale

from PIL import Image
from streamlit_option_menu import option_menu

from paginas.bembolado import pagina_bembolado
from paginas.gerilu import pagina_gerilu
from paginas.gti import pagina_gti


locale.setlocale(locale.LC_ALL, 'pt_BR')

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",

)

with st.sidebar:
    logo_teste = Image.open('logo.png')
    st.image(logo_teste, width=210)
    st.markdown("---")
    selecao = option_menu(
        menu_title="Fechamentos",
        options=["Bem_Bolado", "Gerilu", "Gti"],
        icons=["bar-chart-fill", "bar-chart-fill", "bar-chart-fill"],
        menu_icon="cast",

    )


if selecao == "Bem_Bolado":
    pagina_bembolado()

if selecao == "Gerilu":
    pagina_gerilu()

if selecao == "Gti":
    pagina_gti()