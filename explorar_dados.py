import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import streamlit as st
pio.renderers.default = 'browser'

# Transformação em dataframe e tratamendo dos dados
df = pd.read_csv("dados/student_habits_performance.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
df_clean = df.dropna()
print(df_clean.shape)

# Criando correlação entre variáveis.
df_numeric = df_clean.select_dtypes(include=[np.number])
correlation_matrix = df_numeric.corr()
exam_correlation = correlation_matrix['exam_score'].sort_values(
    ascending=False)
print(exam_correlation)

# Gráfico de correlações

variables = ['study_hours_per_day', 'mental_health_rating',
             'exercise_frequency', 'sleep_hours', 'netflix_hours', 'social_media_hours']

for var in variables:
    fig = px.scatter(df_clean, x=var, y='exam_score', title=f'Relação entre {var} e exam_score',
                     labels={var: var, 'exam_score': 'Pontuação do Exame'},
                     color='exam_score', color_continuous_scale='Viridis')
    fig.show()

    # Salvando o data frame clean
    df_clean.to_csv('dados/df_clean.csv', index=False)
