
#importando as bibliotecas
import pandas as pd
import streamlit as st
import ipeadatapy as ip
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Prova 14_06",
    page_icon="👋",
)
   

df = pd.read_csv("https://raw.githubusercontent.com/jessearodriguesjex/prova14_06/main/projetos-1.csv", sep=";") 
st.dataframe(df)

st.write("Uso do `st.experimental_data_editor()` para edição do dataframe na tela")

code = '''edited_df = st.experimental_data_editor(df, num_rows="dynamic")'''
st.code(code, language='python')

edited_df = st.experimental_data_editor(df, num_rows="dynamic")

"---"  

st.write("Usando `st.checkbox()` para deixar o leitor escolher se vai mostrar a tabela ou não")

code = '''
if st.checkbox('Mostrar dataframe'):
    # usando o streamlit para apresentar como df dinâmico e formatação adicional (max)
    st.dataframe(df.style.highlight_max(axis=0)) 
    '''
st.code(code, language='python')

if st.checkbox('Mostrar dataframe'):
    # usando o streamlit para apresentar como df dinâmico e formatação adicional (max)
    st.dataframe(df.style.highlight_max(axis=0)) 

"---"    

st.write("Adicionando nova linha")

st.code(code, language='python')

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
df = pd.concat([df, df1])
st.write(df)

"---"  

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")

st.code(code, language='python')

st.write(df.groupby('ano').sum())

"---"  

st.write("Geração do gráfico de dispersão cruzando os dados do `Projeto1` e `Projeto2`")

st.code(code, language='python')

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', ax=ax)
st.pyplot(fig)

"---"  

st.write("Criação do gráfico do tipo histograma com os dados do `Projeto 1` e `Projeto4`")

# Geração do gráfico
#fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
st.pyplot(fig)

st.code(code, language='python')

# Geração do gráfico
fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
st.pyplot(fig)
