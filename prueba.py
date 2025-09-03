import time
import sys

# Título
print("-- Calculadora de peso --")

# Entrada de datos
nombre = input("Ingresa tu nombre: ")
peso = input("Ingresa tu peso (kg): ")

# Barra de carga
print("\nCargando datos:")
for i in range(0, 101, 5):
    barra = "#" * (i // 2)
    sys.stdout.write(f"\r[{barra:<50}] {i}%")
    sys.stdout.flush()
    time.sleep(0.1)

# Resultado
print(f"\n\nHola {nombre}, tu peso es: {peso} kg")
print("hola mun")