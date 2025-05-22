import time
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración del generador congruencial lineal
a = 1664525
c = 1013904223
m = 2**32  # número grande, potencia de 2

# Función que genera una variable uniforme [0,1] usando GCL
def generador_uniforme(seed):
    x = (a * seed + c) % m
    return x, x / m

# Obtener una semilla inicial desde el reloj del sistema
semilla = int(time.time() * 1000) % m  # milisegundos actuales

# Generar muestra de tamaño 100
muestra = []
for _ in range(100):
    semilla, u = generador_uniforme(semilla)
    muestra.append(u)

# Histograma y estimación de densidad
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

# Histograma
sns.histplot(muestra, bins=10, kde=True, color='skyblue', stat='density', edgecolor='black')

# Estimación de densidad por núcleo (kde=True ya lo incluye)
plt.title("Histograma y Estimación de Densidad - Uniforme [0,1]")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.show()
