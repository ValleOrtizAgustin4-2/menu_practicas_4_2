# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 19/09/2025
import os
os.system("CLS")

# Generar numeros del 1 al 100
def num_100(n):
    if n <= 100:
        print(n)
        num_100(n + 1)
    
num_100(1)