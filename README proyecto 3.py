# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 22:22:16 2025

@author: melany sanchez
"""

# ⚡️ Análisis y Predicción del Precio Spot de Energía

Este programa permite analizar el comportamiento del precio spot de energía en Colombia y compararlo con datos internacionales. También incluye un modelo predictivo simple basado en regresión lineal.

---

## 🧭 ¿Qué hace el programa?

- Permite ingresar datos manualmente o usar datos simulados.
- Grafica la serie temporal del precio spot por país.
- Muestra relaciones entre variables como embalse, precipitación y combustible.
- Calcula la volatilidad del precio internacional por país.
- Entrena un modelo de regresión para predecir el precio spot en Colombia.
- Muestra el error cuadrático medio (RMSE) del modelo.

---

## ⚙️ Opciones al iniciar

Al ejecutar el programa, se mostrará el siguiente menú:

- Opción 1: carga automáticamente datos simulados.
- Opción 2: permite ingresar datos manualmente desde la consola.

---

## ✍️ Cómo ingresar datos correctamente

### 🇨🇴 Datos para Colombia

Formato por línea:
fecha,precio,embalse,precipitacion,combustible


Ejemplo:
2025-10-01,312.45,58.2,12.3,85.6
al darle enter ingrese los siguientes datos y asi sucesivamente

Cuando termines de ingresar todas las líneas, al darle enter, escribe:   
fin

### 🌍 Datos internacionales

Formato por línea:
fecha,precio,pais


Ejemplo:
2025-10-01,300,Alemania
al darle enter ingrese los siguientes datos y asi sucesivamente

Al finalizar,  al darle enter, escribe:
fin

---

## ⚠️ Requisitos mínimos de datos

Para que el modelo predictivo funcione correctamente:

- Se requieren al menos **3 líneas de datos para Colombia**.
- El modelo elimina la primera fila con `shift()` y filtra nulos con `dropna()`,
 por lo que se necesitan al menos **2 muestras válidas** para entrenar.

Si no se cumplen estos requisitos, el programa mostrará:

⚠️ No hay suficientes datos para entrenar el modelo. Se requieren al menos 2 muestras.

---

## ✅ Recomendaciones

- No mezcles comas con espacios innecesarios.
- Usa el formato de fecha `YYYY-MM-DD`.
- Escribe `fin` en minúsculas y sin espacios para finalizar la entrada.
- Si usas Spyder o Jupyter, asegúrate de que la consola esté activa para ingresar los datos.

---

## 📦 Extensiones posibles

Este programa puede adaptarse fácilmente para:

- Exportar resultados a Excel o CSV.
- Conectarse con fuentes reales como XM, ENTSO-E o ACENOR.
- Convertirse en una app interactiva con Streamlit.




















