import streamlit as st
import joblib

# Cargar el modelo entrenado
model = joblib.load('modelo_entrenado.pkl')

# Crear la interfaz de usuario
st.title("Aplicación de Predicción")
x1 = st.number_input("Valor de Gasto en Educación")
x2 = st.number_input("Valor de tasa de mortalidad infantil")
x3 = st.number_input("Valor del PIB")

# Realizar la predicción
if st.button("Predecir"):
    x_values = [x1, x2, x3]
    prediction = model.predict([x_values])
    st.success(f"La predicción para la esperanza de vida es: {prediction[0]}")


