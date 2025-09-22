# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 19/09/2025
import os
os.system("CLS")

# Sumar digitos
def num_bin(num_dec):
  if num_dec == 0:
    return "0"
  elif num_dec == 1:
    return "1"
  else:
    return num_bin(num_dec // 2) + str(num_dec % 2)
    
num_dec = int(input("Ingresa un numero: "))
print(f"El numero binario de {num_dec} es: {num_bin(num_dec)}")