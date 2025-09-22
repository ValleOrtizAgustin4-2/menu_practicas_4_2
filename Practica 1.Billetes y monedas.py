# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 01/09/2025
import os

os.system("CLS")

cantidad = int(input("Introduzca la cantidad: "))

dinero = {
    "500" : 0,
    "200" : 0,
    "50" : 0,
    "10" : 0,
    "5" : 0,
    "1" : 0
}

for clave, valor in dinero.items():
    v1 = int(clave)
    v2 = int(valor)
    if cantidad >= v1:
        dinero[clave] = cantidad // v1
        cantidad %= v1
            
print("Desglose: ")
for clave, valor in dinero.items():
    v1 = int(clave)
    if v1 >= 50:
        print(f"{valor} billetes de {clave}")
    else:
        print(f"{valor} monedas de {clave}")