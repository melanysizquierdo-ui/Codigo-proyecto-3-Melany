# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 22:06:30 2025

@author: melany sanchez
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
from io import StringIO

# 1. Datos simulados
datos_colombia_simulados = StringIO("""fecha,precio,embalse,precipitacion,combustible
2025-10-01,312.45,58.2,12.3,85.6
2025-10-02,298.70,57.8,11.5,84.9
2025-10-03,305.10,56.9,10.2,86.1
2025-10-04,315.80,55.7,9.8,87.3
2025-10-05,322.65,54.3,8.6,88.0
""")

datos_internacional_simulados = StringIO("""fecha,precio,pais
2025-10-01,200,Francia
2025-10-01,310,Alemania
2025-10-01,355,Chile
2025-10-02,215,Francia
2025-10-02,320,Alemania
2025-10-02,365,Chile
2025-10-03,225,Francia
2025-10-03,330,Alemania
2025-10-03,375,Chile
""")

# 2. Ingreso manual
def ingresar_datos_colombia():
    print("\nIngrese datos para Colombia (fecha,precio,embalse,precipitacion,combustible). Escriba 'fin' para terminar.")
    datos = []
    while True:
        entrada = input("Ejemplo: 2025-10-01,312.45,58.2,12.3,85.6 → ")
        if entrada.lower().strip() == "fin":
            break
        try:
            fecha, precio, embalse, precipitacion, combustible = entrada.split(",")
            datos.append({
                "fecha": pd.to_datetime(fecha.strip()),
                "precio": float(precio),
                "embalse": float(embalse),
                "precipitacion": float(precipitacion),
                "combustible": float(combustible)
            })
        except:
            print("⚠️ Formato inválido. Intente de nuevo.")
    return pd.DataFrame(datos)

def ingresar_datos_internacionales():
    print("\nIngrese datos internacionales (fecha,precio,pais). Escriba 'fin' para terminar.")
    datos = []
    while True:
        entrada = input("Ejemplo: 2025-10-01,300,Alemania → ")
        if entrada.lower().strip() == "fin":
            break
        try:
            fecha, precio, pais = entrada.split(",")
            datos.append({
                "fecha": pd.to_datetime(fecha.strip()),
                "precio": float(precio),
                "pais": pais.strip()
            })
        except:
            print("⚠️ Formato inválido. Intente de nuevo.")
    return pd.DataFrame(datos)

# 3. Visualización
def graficar_series(df_col, df_int):
    plt.figure(figsize=(10, 5))
    plt.plot(df_col["fecha"], df_col["precio"], label="Colombia", linewidth=2)
    for pais in df_int["pais"].unique():
        datos = df_int[df_int["pais"] == pais]
        plt.plot(datos["fecha"], datos["precio"], label=pais, linestyle="--")
    plt.title("Serie Temporal del Precio Spot")
    plt.xlabel("Fecha")
    plt.ylabel("Precio (USD/MWh)")
    plt.legend()
    plt.tight_layout()
    plt.show()

def graficar_relaciones(df):
    df = df.dropna()
    sns.pairplot(df[["precio", "embalse", "precipitacion", "combustible"]])
    plt.suptitle("Relación entre Precio Spot y Variables Clave", y=1.02)
    plt.show()

def graficar_volatilidad(df_int):
    volatilidad = df_int.groupby("pais")["precio"].std().reset_index()
    sns.barplot(data=volatilidad, x="pais", y="precio")
    plt.title("Volatilidad del Precio Spot por País")
    plt.ylabel("Desviación Estándar")
    plt.tight_layout()
    plt.show()

# 4. Modelo predictivo
def modelo_lineal(df):
    df = df.dropna()
    df["mes"] = df["fecha"].dt.month
    df["precio_lag1"] = df["precio"].shift(1)
    df = df.dropna(subset=["precio_lag1"])

    if df.shape[0] < 2:
        print("⚠️ No hay suficientes datos para entrenar el modelo. Se requieren al menos 2 muestras.")
        return

    X = df[["precio_lag1", "embalse", "mes"]]
    y = df["precio"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    rmse = root_mean_squared_error(y_test, y_pred)
    print(f"\n📉 Error cuadrático medio (RMSE): {rmse:.2f}")

# 5. Menú de selección
def seleccionar_modo():
    print("¿Cómo deseas ingresar los datos?")
    print("1. Usar datos simulados")
    print("2. Ingresar datos manualmente")
    opcion = input("Selecciona 1 o 2 → ")
    if opcion.strip() == "2":
        df_col = ingresar_datos_colombia()
        df_int = ingresar_datos_internacionales()
    else:
        df_col = pd.read_csv(datos_colombia_simulados, parse_dates=["fecha"])
        df_int = pd.read_csv(datos_internacional_simulados, parse_dates=["fecha"])
    return df_col, df_int

# 6. Ejecución principal
if __name__ == "__main__":
    df_col, df_int = seleccionar_modo()
    if not df_col.empty and not df_int.empty:
        graficar_series(df_col, df_int)
        graficar_relaciones(df_col)
        graficar_volatilidad(df_int)
        modelo_lineal(df_col)
    else:
        print("⚠️ No se ingresaron datos suficientes para continuar.")