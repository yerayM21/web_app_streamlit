import streamlit as st 
import pandas as pd 
import plotly_express as px

#configuracion de la barra de navegacion
st.set_page_config(page_title="Proyecto vehicular", page_icon=':car:', layout='centered')

#Encabezado
st.header('Registro de vehiculos')

#se lee el conjunto de datos de vehiculos
car_data = pd.read_csv('/programacion/web_streamlit/web_app_streamlit/Data_set/vehicles_us.csv')

# Selección de categoría
categoria_seleccionada = st.selectbox("Seleccione la categoría", car_data.columns)

#Barra lateral para seleccion
ticker = st.sidebar.text_input('ticker')


#Creacion de histograma en base a la columna seleccionada 
if categoria_seleccionada:
    st.write('creacion de un histograma para el conjunto de datos selecionado')

    fig = px.histogram(car_data, x= categoria_seleccionada)

    st.plotly_chart(fig,use_container_width=True)



#creacion de botones para histograma 
hist_button = st.button('construir histograma')

# condiciones para la ejecucion de boton
if hist_button:
    st.write('Creacion de un histograma del kilometraje de los vehiculos')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig,use_container_width=True)

#Creacion de checkbox para diagrama de dispercion 
scatter_checkbox =st.checkbox('construir una grafica de dispercion ')  

if scatter_checkbox:
    st.write('creacion de grafica de dispercion del kilometraje de los vehiculos y como este afecta el precio')

    fig = px.scatter(car_data, x='odometer' , y='price')

    st.plotly_chart(fig,use_container_width=True)