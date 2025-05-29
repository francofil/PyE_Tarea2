import pandas as pd
import matplotlib.pyplot as plt

#Leemos archivo
archivo = pd.read_csv("Parte1/cancelaciones.csv")


#Graficamos con funcion matpltlin

plt.hist(archivo["cancelaciones"], range(archivo["cancelaciones"].min(), archivo["cancelaciones"].max()))
plt.title('Histograma de Cancelaciones Diarias')
plt.xlabel('Cantidad de cancelaciones')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()