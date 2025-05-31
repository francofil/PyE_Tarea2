import os
import pandas as pd
import matplotlib.pyplot as plt

#Leemos archivo
ruta = os.path.join(os.path.dirname(__file__), "cancelaciones.csv")
archivo = pd.read_csv(ruta)
#Graficamos con funcion matpltlin

plt.hist(archivo["cancelaciones"], range(archivo["cancelaciones"].min(), archivo["cancelaciones"].max()))
plt.title('Histograma de Cancelaciones Diarias')
plt.xlabel('Cantidad de cancelaciones')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()