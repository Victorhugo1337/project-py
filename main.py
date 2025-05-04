import pandas as pd
import streamlit as st
import plotly.express as px

# Dataset clean
df_clean = pd.read_csv('dados/df_clean.csv')


variables = ['study_hours_per_day', 'mental_health_rating',
             'exercise_frequency', 'sleep_hours', 'netflix_hours', 'social_media_hours']

# Definir título do dashboard
st.title("Dashboard de Análise das Variáveis em Relação ao Exame")

for var in variables:
    fig = px.scatter(df_clean, x=var, y='exam_score', title=f'Relação entre {var} e exam_score',
                     labels={var: var, 'exam_score': 'Pontuação do Exame'},
                     color='exam_score', color_continuous_scale='Viridis')
    st.plotly_chart(fig)
