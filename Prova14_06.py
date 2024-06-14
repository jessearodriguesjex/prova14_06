
import pandas as pd  
import streamlit as st


# título na barra do navegador
st.set_page_config(
page_title="Prova 14_06 - Exercício Projetos",
  
)

st.header("Dados do Projeto")
arquivo = "https://raw.githubusercontent.com/jessearodriguesjex/prova14_06/main/projetos-1.csv" 
df = pd.read_csv(arquivo, sep=';') 
st.dataframe(dfe)


st.write("Adicionando a ultima linha")

df1 = pd.DataFrame({'mes': [12], 'ano': [2023], 'Projeto1': [29376], 'Projeto2': [40392], 'Projeto3': [63648], 'Projeto4': [29376], 'Projeto5': [25704] })
dfe = pd.concat([df, df1])
st.write(dfe)

st.code(code, language='python')

st.write("Apresentação da soma dos valores de cada projeto agrupado por ano")

st.write(df.groupby('ano').sum())

"---"  

st.write("Geração do gráfico de dispersão cruzando os dados do `Projeto1` e `Projeto2`")

st.code(code, language='python')

fig, ax = plt.subplots()
df.plot(kind = 'scatter', x = 'Projeto1', y = 'Projeto2', ax=ax)
st.pyplot(fig)

"---"  

# Geração do gráfico
fig, ax = plt.subplots()
df["Projeto1"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
#st.pyplot(fig)

# Geração do gráfico
#fig, ax = plt.subplots()
df["Projeto4"].plot(kind='hist', ax=ax)
# Exibição do gráfico no Streamlit
st.pyplot(fig)
