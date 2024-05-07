import streamlit as st
import sys
import os

# Adicione o diretório do módulo ao caminho do sistema
sys.path.append(os.path.dirname(__file__))

# Importe a função load_data do módulo banco
from banco import load_data

def pagina_bembolado():
    st.title("Bembolado")
    df_geral = load_data()
    st.dataframe(df_geral)




















# import streamlit as st
# import sys
# import os
#
# # Adiciona o diretório atual ao caminho do sistema
# sys.path.append(os.path.dirname(__file__))
#
# from paginas.banco import load_data
#
# def pagina_bembolado():
#     st.title("Bembolado")
#     df_geral = load_data()
#     st.dataframe(df_geral)

