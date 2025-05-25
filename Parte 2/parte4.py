import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generador congruencial lineal
a = 1664525
c = 1013904223
m = 2**32

# Función para generar uniforme [0,1]
def generador_uniforme(seed):
    x = (a * seed + c) % m
    return x, x / m

# Inicializar semilla
semilla = int(time.time() * 1000) % m

# Parte 4: Generar muestra de Cauchy estándar a partir de uniforme
muestra_cauchy = []
for _ in range(100):
    semilla, u = generador_uniforme(semilla)
    x = np.tan(np.pi * (u - 0.5))  # Transformación inversa de la CDF
    muestra_cauchy.append(x)

# Gráfico de histograma y densidad (acotado para mejor visualización)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.histplot(muestra_cauchy, bins=30, kde=True, color='lightcoral', stat='density', edgecolor='black')

# Superponer la densidad teórica
x_vals = np.linspace(-25, 25, 1000)
densidad_teorica = 1 / (np.pi * (1 + x_vals**2))
plt.plot(x_vals, densidad_teorica, color='darkred', label='Densidad Cauchy estándar')

plt.xlim(-25, 25)
plt.title("Muestra Cauchy Estándar - Histograma + Densidad (acotado)")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.show()
