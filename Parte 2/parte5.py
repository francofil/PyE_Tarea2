import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# ---------- Parte 2 (Generador uniforme y muestra de tamaño 100) ----------

a = 1664525
c = 1013904223
m = 2**32  # módulo grande

def generador_uniforme(seed):
    x = (a * seed + c) % m
    return x, x / m

semilla = int(time.time() * 1000) % m
muestra = []
for _ in range(100):
    semilla, u = generador_uniforme(semilla)
    muestra.append(u)

# ---------- Parte 5 (Transformar a Cauchy y graficar) ----------

# Transformación inversa de la CDF de la Cauchy estándar
muestra_cauchy = [np.tan(np.pi * (u - 0.5)) for u in muestra]

# Gráfico: Histograma + KDE + densidad teórica
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

sns.histplot(muestra_cauchy, bins=30, kde=True, color='lightcoral', stat='density', edgecolor='black')

# Densidad teórica Cauchy estándar
x_vals = np.linspace(-25, 25, 1000)
densidad_teorica = 1 / (np.pi * (1 + x_vals**2))
plt.plot(x_vals, densidad_teorica, color='darkred', label='Densidad Cauchy estándar')

# Ajustes finales
plt.xlim(-25, 25)
plt.title("Parte 5 - Muestra Cauchy Estándar desde Uniformes [0,1]")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.tight_layout()
plt.show()
