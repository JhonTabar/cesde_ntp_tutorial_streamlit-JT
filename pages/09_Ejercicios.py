import streamlit as st
import random
import pandas as pd
import numpy as np
from numpy.random import default_rng as rng


st.subheader("Ejercicio 1: Simple Saludo")

nombre = st.text_input("Ingrese su nombre", "")
if nombre:
    st.write(f"¡Hola, {nombre}!")

st.divider()

st.subheader("Ejercicio 2: Calculadora de Producto")

num1 = st.number_input("Ingrese numeros para multiplicar", 0)
num2 = st.number_input("Ingrese el segundo numero", 0)
resultado = num1 * num2
st.write(f"El resultado es: {resultado}")  
if num1 >= 100.0 or num2 >= 100.0:
    st.warning("Números grandes!")

st.divider()
    
st.subheader("Ejercicio 3: Convertidor de Temperatura")

def convertidorTemp ():
    heater = st.radio("Seleccione la conversión", ("Celsius a Fahrenheit", "Fahrenheit a Celsius"))
    temp = st.number_input("Ingrese la temperatura a convertir", 0.0)
    if heater == "Celsius a Fahrenheit":
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9
st.write(f"La temperatura convertida es: {convertidorTemp()}")

st.divider()

st.subheader("Ejercicio 4: Galeria de Mascotas")

tab1, tab2, tab3 = st.tabs(["Ave", "Gato", "Perro"])
with tab1:
    st.header("Una cacatúa")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/60/Cockatiel_kept_as_pet.jpg", width=200)  
with tab2:
    st.header("Un gato")
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5b/White_cat_drinking_from_a_gold_fish_pond..jpg", width=200)
with tab3:
    st.header("Un perro")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/31/Bo_official_portrait_%28cropped_2%29.jpg", width=200)

if st.button("Me gusta!"):
    st.toast("Te gusta esta mascota.")

st.divider()

st.subheader("Ejercicio 5: Caja de Comentarios")

with st.form("Comentarios"):
    asuntocom = st.text_input("Asunto")
    comment = st.text_area("Escribe tus comentarios aquí")
    submit = st.form_submit_button("Enviar")
if comment and submit:
    st.json(
        {"Asunto": {asuntocom},
         "Comentario": {comment}
        }
    )

st.divider()

st.subheader("Ejercicio 6: Login Simulado")

def Login():
    if "usuario" not in st.session_state:
        st.session_state["usuario"] = ""
    if "contrasena" not in st.session_state:
        st.session_state["contrasena"] = ""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    st.write(st.session_state.usuario)
    st.write(st.session_state.contrasena)

    

with st.form("Login"):

    username = st.text_input("Usuario", key="usuario")
    password = st.text_input("Contraseña", type="password", key="contrasena")
    ingresar = st.form_submit_button(label = "Ingresar", on_click=Login)
if ingresar and username == "admin" and password == "1234":
    st.success("¡Bienvenido, admin!")
    st.write(st.session_state.usuario + " " + st.session_state.contrasena)
    st.session_state.logged_in = True
    logout = st.button(label = "Cerrar Sesión")
    if logout:
     del st.session_state.usuario, st.session_state.contrasena
     st.session_state.logged_in = False
    #st.write(st.session_state.usuario + " " + st.session_state.contrasena)
elif ingresar and (username != "admin" or password != "1234"):
        st.error("Usuario o contraseña incorrectos.")
else: 
    st.error("Campos vacios: Iniciar sesion.")

st.divider()

st.subheader("Ejercicio 7: Lista de Compras")

def AgregarItem():
    st.session_state.item.append(st.session_state.item_input)

def SesionLista():
 if 'item' not in st.session_state:
    st.session_state.item = []

SesionLista()

with st.form("Lista de Compras"):
    iteminput = st.text_input("Agregar Item", key = "item_input")
    agregar = st.form_submit_button("Agregar a la lista", on_click=AgregarItem)
    limpiar = st.form_submit_button("Limpiar lista")
if limpiar:
    st.session_state.item = []
else:
    st.error("Campos vacios: Agregar Items")

st.write(st.session_state.item)

st.divider()

st.subheader("Ejercicio 8: Gráfico Interactivo")

values = st.slider("Select a range of values", 10, 100)
st.write("Values:", values)

n = values 
rng = np.random.default_rng()
li = rng.integers(10, 100, size=n).tolist()

print(li)

st.line_chart(
    li,
    color=["#FF0000"]
 )

if st.button("Regenerar", key="regenerar"):
  st.rerun()





