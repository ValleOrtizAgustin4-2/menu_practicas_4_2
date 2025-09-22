# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 19/09/2025
import os
os.system("CLS")

# Invertir frases
def invert_frase(frase):
    if len(frase) == 0:
        return frase
    else:
        return frase[-1] + invert_frase(frase[:-1])
    
frase = str(input("Ingresa una frase: "))
print(invert_frase(frase))