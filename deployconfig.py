import streamlit as st
import plotly.express as px
import pandas as pd
import joblib
#------------para facilitar edição
#.\ambv\Scripts\activate
#streamlit run deployconfig.py

#para comitt:
# git remote add origin https://github.com/Nic62/Cluster_Credito.git
#git branch -M main
#git push -u origin main
# joblib.load('kbirch.pkl')
st.title("Agrupador de Crédito")
st.divider()
st.header('Digite as informações abaixo:')
info_LimitedeCrédito=st.number_input("Digite o Limite do seu cartão")
st.write("seu limite é :", info_LimitedeCrédito)
info_TotaldeCartõesCredito=st.select_slider("Selecione o numero de cartões de crédito",["1","2","3","4","5","6","7","8","9","10+"])
if info_TotaldeCartõesCredito == "10+":
    st.number_input('Se maior que dez quantos :',10)
st.write("Você possui:", info_TotaldeCartõesCredito)

info_NúmeroTotal=st.number_input("Quantas visitas ja fez ao banco:", 0, 100, step=1)
st.write("Vocêvisitou:", info_NúmeroTotal)
info_online=st.number_input("Quantas visitas ja fez online:", 0, 100, step=1)
st.write("Você visitou:", info_online)
info_Totalchamadas=st.number_input("Quantidade de chamadas:", 0, 100, step=1)
st.write("Você realizou:", info_Totalchamadas)
st.divider()
bb=st.button("Agrupar")
if bb:
    df_predicao=pd.DataFrame({
        'Limite de Crédito Médio': [info_LimitedeCrédito],
        'Total de Cartões Credito':[info_TotaldeCartõesCredito],
        'Número Total de Visitas ao Banco':[info_NúmeroTotal],
        'Total de visitas online':[info_online],
        'Total de chamadas realizadas':[info_Totalchamadas]
        })
    
    st.dataframe(df_predicao)