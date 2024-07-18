import streamlit as st
import plotly.express as px
#------------para facilitar edição
#.\ambv\Scripts\activate
#streamlit run deployconfig.py
# freatures:
# Limite de Crédito Médio
# Total de Cartões Credito	
# Número Total de Visitas ao Banco	
# Total de visitas online	
# Total de chamadas realizadas

# joblib.load("kbirch.pkl")
st.title("Agrupador de Crédito")
st.header('Digite as informações abaixo:')
info_LimitedeCrédito=st.
info_TotaldeCartõesCredito=st.select_slider("Selecione o numero de cartões de crédito")
st.write("Você possui:", info_TotaldeCartõesCredito)
info_NúmeroTotaldeVisitasaoBanco
info_Totaldevisitasonline
info_Totaldechamadasrealizadas
