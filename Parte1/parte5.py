import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# Leer archivo CSV 
ruta = os.path.join(os.path.dirname(__file__), "cancelaciones.csv")
df = pd.read_csv(ruta)

cancelaciones = df['cancelaciones']

#Calcular lambda
lambda_ = cancelaciones.mean()

plt.hist(cancelaciones, bins=range(cancelaciones.min(), cancelaciones.max() + 2), density=True, alpha=0.6, edgecolor='black', label="Datos reales")

#función de masa de probabilidad
x_vals = np.arange(cancelaciones.min(), cancelaciones.max() + 1)
pmf_vals = poisson.pmf(x_vals, mu=lambda_)

#superpone lambda coon el histograma
plt.plot(x_vals, pmf_vals, 'o-', color='red', label=f'Distribución de Poisson (λ={lambda_:.2f})')

# 🎨 Detalles del gráfico
plt.title('Cancelaciones diarias vs. Distribución de Poisson')
plt.xlabel('Cantidad de cancelaciones por día')
plt.ylabel('Probabilidad (densidad)')
plt.legend()
plt.grid(True)
plt.show()
