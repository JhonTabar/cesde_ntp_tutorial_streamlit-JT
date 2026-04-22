import streamlit as st


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
