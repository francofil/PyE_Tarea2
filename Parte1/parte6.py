import math
import os
import pandas as pd

ruta = os.path.join(os.path.dirname(__file__), "cancelaciones.csv")
df = pd.read_csv(ruta)

cancelaciones = df['cancelaciones']
def poisson_pmf(k, lmbda):
    return (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)

lambda_ = cancelaciones.mean()

# menos de 5 cancelaciones en un dia entooces => (X < 5) = P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4)
p_menor_5_manual = sum(poisson_pmf(k, lambda_) for k in range(5))

# P(X > 15) = 1 - P(X <= 15)
p_mayor_15_manual = 1 - sum(poisson_pmf(k, lambda_) for k in range(16))

print("Menos de 5 cancelaciones en un dia entooces => (X < 5) = P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4)")
print(f"P(X < 5) = {p_menor_5_manual:.4f}")
print("Mas de 15 cancelaciones en un dia entooces => P(X>15) = 1− P(X≤15)")
print(f"P(X > 15) = {p_mayor_15_manual:.4f}")
