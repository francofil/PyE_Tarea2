import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("Parte 1/cancelaciones.csv")
cancelaciones = datos["cancelaciones"]


#frecuencia absoluta
frecuencia = cancelaciones.value_counts().sort_index()

#frecuencia relativa 
total_dias = len(cancelaciones)
probabilidad = frecuencia / total_dias

#distribución acumulada
distribucion_acumulada = probabilidad.cumsum()

print("Cantidad | Frecuencia | Probabilidad | Acumulada")
for valor in frecuencia.index:
    print(f"{valor:9} | {frecuencia[valor]:10} | {probabilidad[valor]:11.3f} | {distribucion_acumulada[valor]:9.3f}")

media = cancelaciones.mean()
varianza = cancelaciones.var()

print("\nMedia (esperanza empírica):", round(media, 2))
print("Varianza empírica:", round(varianza, 2))

mediana = cancelaciones.median()
q1 = cancelaciones.quantile(0.25)
q3 = cancelaciones.quantile(0.75)
iqr = q3 - q1

print("\nMediana:", mediana)
print("IQR (rango intercuartílico):", iqr)

