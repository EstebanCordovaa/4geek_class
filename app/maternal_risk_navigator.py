import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
import pickle

with open('/workspaces/4geek_class/models/model_maternal_risk.pkl', 'rb') as file:
    df = pickle.load(file)

st.title('Maternal Risk Navigator')
st.dataframe(df.sample(10, random_state=2025))
st.markdown('## Hallazgos')
st.markdown('Podemos observar en la variable age que los rangos estan dentro de ** 15 y 55 ** años. Esto significa que contamos con embarazos juveniles y de etapa tardia')
st.dataframe(df.describe(include= 'number').T)
fig = px.scatter_matrix(df,dimensions=['age', 'systolicbp', 'diastolicbp',], color='risklevel')
#fig = px.scatter_matrix(
    #df[['age', 'systolicbp', 'diastolicbp', 'risklevel']], 
    #color='risklevel', 
    #width=1200,  # Ajusta el ancho en píxeles
    #height=800   # Ajusta la altura en píxeles
#)
st.plotly_chart(fig)
fig_2 = px.parallel_coordinates(df, color_continuous_scale= px.colors.diverging.Tealrose, color= df['risklevel'].map({'high_risk':0, 'low_risk':1, 'mid_risk':2})) 
st.plotly_chart(fig_2)
fig_3 = pd.plotting.parallel_coordinates(df.sample(90, random_state=2025), 'risklevel', color=['teal', 'gold', 'crimson'])
st.pyplot(pd.plotting.parallel_coordinates(df.sample(90, random_state=2025), 'risklevel', color=['teal', 'gold', 'crimson']))