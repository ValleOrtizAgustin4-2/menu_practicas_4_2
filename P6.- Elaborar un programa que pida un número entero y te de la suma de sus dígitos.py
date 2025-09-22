# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 19/09/2025
import os
os.system("CLS")

# Sumar digitos
def sumar_digitos(num):
  if len(num) == 0:
    return 0
  else:
    num_1 = int(num[0])
    nums = num[1:]
    return num_1 + sumar_digitos(nums)
    
num = str(input("Ingresa un numero: "))
print(f"La suma de los dígitos es: {sumar_digitos(num)}")