import pandas as pd
import nbformat
import plotly_express as px
import streamlit as st

data_vehicle = pd.read_csv(
    "../vehicles_us.csv")
# leer los datos


st.header("Vehicle Market")
st.write('Description of vehicles for sale.')
hist_button = st.button('Vehicle Mileage')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Vehicle Mileage')

    # crear un histograma
    fig = px.histogram(data_vehicle, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    hist_button = st.button('Back')  # regresa a menu

hist_button = st.button(
    'Price of the vehicle in relation to its miles traveled.')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Price-Use Ratio')

    # crear un histograma
    # crear un gráfico de dispersión
    fig = px.scatter(data_vehicle, x="odometer", y="price")
    fig.show()  # crear gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    hist_button = st.button('Back')  # regresa a menu

hist_button = st.button('Price-Condition Ratio')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Price of the vehicle in relation to its condition.')

    price_Condition = data_vehicle.groupby("condition", as_index=False)["price"].mean(
        # agrupamos por condicion y promedio de precio
    ).sort_values(by="price", ascending=False)
    fig = px.histogram(price_Condition, x="condition", y="price", color="condition", color_discrete_map={
        "new": "green",
        "like new": "blue",
        "excellent": "purple",
        "good": "orange",
        "fair": "red",
        "salvage": "black"
    })  # crear un gráfico de dispersión
    fig.show()  # crear gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    hist_button = st.button('Back')  # regresa a menu

show_chart = st.checkbox('Show Vehicles')

if show_chart:  # si la casilla de verificación está seleccionada
    st.write('Vehicles for sales')

    data_vehicle  # muestra los autos en venta
