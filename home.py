import streamlit as st
import locale
from PIL import Image
from streamlit_option_menu import option_menu

# Configure a localidade
locale.setlocale(locale.LC_ALL, 'pt_BR')

# Configurações da página
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
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

# Verifica a seleção e chama a função correspondente
if selecao == "Bem_Bolado":
    # Importe a função pagina_bembolado do módulo bembolado
    from paginas.bembolado import pagina_bembolado
    pagina_bembolado()

elif selecao == "Gerilu":
    # Importe a função pagina_gerilu do módulo gerilu
    from paginas.gerilu import pagina_gerilu
    pagina_gerilu()

elif selecao == "Gti":
    # Importe a função pagina_gti do módulo gti
    from paginas.gti import pagina_gti
    pagina_gti()

















# import streamlit as st
# import locale
#
# from PIL import Image
# from streamlit_option_menu import option_menu
#
# from paginas.bembolado import pagina_bembolado
# from paginas.gerilu import pagina_gerilu
# from paginas.gti import pagina_gti
#
#
# locale.setlocale(locale.LC_ALL, 'pt_BR')
#
# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#
# )
#
# with st.sidebar:
#     logo_teste = Image.open('logo.png')
#     st.image(logo_teste, width=210)
#     st.markdown("---")
#     selecao = option_menu(
#         menu_title="Fechamentos",
#         options=["Bem_Bolado", "Gerilu", "Gti"],
#         icons=["bar-chart-fill", "bar-chart-fill", "bar-chart-fill"],
#         menu_icon="cast",
#
#     )
#
#
# if selecao == "Bem_Bolado":
#     pagina_bembolado()
#
# if selecao == "Gerilu":
#     pagina_gerilu()
#
# if selecao == "Gti":
#     pagina_gti()