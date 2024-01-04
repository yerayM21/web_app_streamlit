import streamlit as st 
import pandas as pd 
import plotly_express as px

#configuracion de la barra de navegacion
st.set_page_config(page_title="Proyecto vehicular", page_icon=':car:', layout='centered')

#Encabezado
st.header('Registro de vehiculos')

#se lee el conjunto de datos de vehiculos
car_data = pd.read_csv('Data_set/vehicles_us.csv')

#Filtrar los años
filter_year = sorted(car_data['model_year'].unique())

#seleccion de año del carro
año_seleccionado = st.selectbox("**Selecciones el año del carro que desea**",filter_year,key='SelecionAño')

if año_seleccionado:
    total_carros_año = car_data['model_year'][(car_data['model_year'] == año_seleccionado)].count()
    st.write(f"Existe {total_carros_año} carros del año {año_seleccionado}")
    # Filtrar datos para el año seleccionado 
    carros_del_año = car_data[(car_data['model_year'] == año_seleccionado)].head(10)

    # Mostrar tabla de los 10 primeros carros para el año seleccionado
    st.write(f"**Estos son los primeros 10 carros para el año {año_seleccionado}:**")
    st.write(carros_del_año)


# Selección de categoría
categoria_seleccionada = st.selectbox("Seleccione la categoría", car_data.columns)

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