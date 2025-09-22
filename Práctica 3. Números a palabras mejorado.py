# Autor: Agustín Eduardo Valle Ortiz
# Grupo: TIDS 4 -2
# Fecha: 05/09/2025
import os
os.system("CLS")
# Numeros en palabras
def numeros_palabras(n):
    unidades = [
        "", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
        "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
        "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
        "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"
        ]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    
    def tres_tres(numero):
        if numero == 0:
            return ""
        if numero == 100:
            return "cien"
        cent = numero // 100
        rest = numero % 100
        dece = rest // 10
        uni = rest % 10
        palabra = ""
        
        if cent > 0:
            palabra = centenas[cent]
        if rest > 0:
            if palabra != "":
                palabra = palabra + " "
            if rest < 30:
                palabra = palabra + unidades[rest]
            else:
                if uni > 0:
                    palabra = palabra + decenas[dece] + " y " + unidades[uni]
                else:
                    palabra = palabra + decenas[dece]
        return palabra
    
    if n == 0:
        return "cero"
    
    respuesta = ""
    
    mil_millones = n // 1000000000
    n = n % 1000000000
    if mil_millones > 0:
        if mil_millones == 1:
            respuesta = respuesta + "mil millones"
        else:
            respuesta = respuesta + tres_tres(mil_millones) + " mil millones"
    if respuesta != "" and n > 0:
        respuesta = respuesta + " "
    
    millones = n // 1000000
    n = n % 1000000
    if millones > 0:
        if millones == 1:
            respuesta = respuesta + "un millon"
        else:
            respuesta = respuesta + tres_tres(millones) + " millones"
        if respuesta != "" and n > 0:
            respuesta = respuesta + " "
    
    miles = n // 1000
    n = n % 1000
    if miles > 0:
        if miles == 1:
            respuesta = respuesta + "mil"
        else:
            respuesta = respuesta + tres_tres(miles) + " mil"
    if respuesta != "" and n > 0:
        respuesta = respuesta + " "
    if n > 0:
        respuesta = respuesta + tres_tres(n)
    return respuesta
    
n = int(input("Introduce un numero del 0 al 999999999999: "))
while n < 0 or n > 999999999999:
    n = int(input("Introduce un numero del 0 al 999999999999: "))
else:
    print(numeros_palabras(n))