# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 05/09/2025
import os
os.system("CLS")
def palabra_completa(copia_num):
    unidades = [
        "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
        "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
        "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
        "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"
        ]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if copia_num == 100:
        return "cien"

    if copia_num < 30:
        return unidades[copia_num]
    
    if copia_num < 100:
        dec = copia_num // 10
        uni = copia_num % 10
        if uni == 0:
            return decenas[dec]
        else:
            return f"{decenas[dec]} y {unidades[uni]}"
    
    cen = copia_num // 100
    restante = copia_num % 100
    if restante == 0:
        return "cien" if n == 100 else centenas[cen]
    else:
        return f"El numero es: {centenas[cen]} {palabra_completa(restante)}"

cent = 0
dece = 0
unid = 0    
numero = int(input("Introduce un numero del 0 al 999: "))
while numero < 0 or numero > 999:
    numero = int(input("Introduce un numero del 0 al 999: "))
else:
    copia_num = numero
    while numero > 0:
        if numero >= 100:
            numero -= 100
            cent += 1
                    
        elif numero <= 99 and numero >= 10:
            numero -= 10
            dece += 1
                    
        elif numero <= 9 and numero > 0:
            numero -= 1
            unid += 1
    
print(f"{cent} centenas {dece} decenas {unid} unidades")
print(palabra_completa(copia_num))