import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_ods_reader import read_ods


uploaded_file = st.sidebar.file_uploader("Choose a xlsx file", type="ods")

if uploaded_file is not None:
  df = read_ods(uploaded_file,1)
  #df = pd.read_excel(uploaded_file, index_col=0)
  #df = pd.read_excel(uploaded_file, delimiter=";", encoding='utf-8')

  df = df.drop(columns=['Número de identificação', 'Sobrenome','Instituição', 'Departamento', 'Endereço de email', 'Último download realizado neste curso.'])
  df = df.set_index('Nome')
  df = df.replace('-',0.0)

  [lin, col] = df.shape

  st.title('Dashboard Quiz')
  st.write('Quantidade de Quizz na Disciplina: ', col)
  st.write('Número de Alunos ', lin)

  st.header('Notas')
  st.write(df)

  coluna = df.columns
  st.header('Média')
  st.table(df.mean())

  df1_transposed = df.reset_index()

  x = st.selectbox('Escolha o Quiz',coluna)  # 👈 this is a widget

  [lin, col] = df.shape
  index = np.arange(lin)
  plt.bar(index, df[x])
  plt.xlabel('Aluno', fontsize=5)
  plt.ylabel('Nota Quiz', fontsize=5)
  plt.xticks(index, df.index, fontsize=5, rotation=30)
  plt.title(x)

  st.pyplot()

  vetor = []
  for i in df.index:
    vetor = [vetor, i];


  options = st.multiselect('Escolha o Alunos', df1_transposed['Nome'])

  for i in options:
    plt.plot(np.arange(col), df.loc[i].T, label=i)
  plt.xlabel('QUIZ')
  plt.ylabel('NOTA')
  plt.legend()
  st.pyplot()

