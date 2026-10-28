import random
import utilidades

# Gera lista com 10 números aleatórios
lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

print("Lista gerada:")
print(lista)

print("\nMaior número (Iterativo):")
print(utilidades.maior_iterativo(lista))

print("\nMaior número (Recursivo):")
print(utilidades.maior_recursivo(lista))
