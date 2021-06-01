import numpy as np
import pandas as pd
from random import randint

# Autor
# Bastian Silva
# Clase
# Inferencia Estadistica


def calcular_Promedio(datos_str):
    lista = datos_str.split()
    nueva_lista = []
    # Recorrer lista y convertir los valores a flotantes
    for i in lista:
        nueva_lista.append(float(i))

    array = np.array(nueva_lista)
    print("\npromedio: ", array.mean(), "\n")


def importar_Excel(ruta, nombre_Hoja, nombre_columna):
    df = pd.read_excel(ruta, sheet_name=nombre_Hoja)
    # Elejir columna
    columna = df[nombre_columna]
    return columna


def muestra_Aleatoria(lista_Datos, meses, numero_filas, datos):
    for i in range(meses):
        # Añadir aleatoriamente a una lista algun dato de esa columna
        lista_Datos.append(round(datos[randint(0, numero_filas)], 2))
    return lista_Datos


def estadidisticas(datos_aleatorios):
    array_datos = np.array(datos_aleatorios)
    promedio = round(array_datos.mean(), 2)
    desv_est_muestral = round(array_datos.std(ddof=1), 2)

    print("\nPromedio:", promedio,
          "Desviacion Estandar Muestral:", desv_est_muestral)


# Pregunta 1 Calcular el promedio de la estimacion lambda
print("-----PREGUNTA 1-----")
calcular_Promedio(
    "0,92 0,79 0,90 0,65 0,86 0,47 0,73 0,97 0,94 0,77".replace(",", "."))


# Pregunta 2
print("-----PREGUNTA 2-----\n")
calcular_Promedio(
    "3,11 0,64 2,55 2,20 5,44 3,42 10,39 8,93 17,82 1,30".replace(",", "."))

# Pregunta 3: generar muestra aleatoria simple a partir de los datos
print("-----PREGUNTA 3-----\n")
datos_produccion_Bienes = importar_Excel(
    'BBDD Prueba asincrónica.xlsx', 'Cuadro', '2.Producción de bienes')

# Llamado de funciones para imprimir los datos en pantalla
datos_aleatorios = muestra_Aleatoria([], 20, 253, datos_produccion_Bienes)

print("--Datos--\n", datos_aleatorios)

estadidisticas(datos_aleatorios)

datos_produccion_Mineria = importar_Excel(
    'BBDD Prueba asincrónica.xlsx', 'Cuadro', '3.Minería')

datos_aleatorios = muestra_Aleatoria([], 20, 253, datos_produccion_Mineria)

print("\n--Datos--\n", datos_aleatorios)

estadidisticas(datos_aleatorios)

datos_produccion_Industria = importar_Excel(
    'BBDD Prueba asincrónica.xlsx', 'Cuadro', '4.Industria')

datos_aleatorios = muestra_Aleatoria([], 20, 253, datos_produccion_Industria)

print("\n--Datos--\n", datos_aleatorios)

estadidisticas(datos_aleatorios)
