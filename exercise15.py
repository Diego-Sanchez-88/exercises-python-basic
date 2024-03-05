# Ejercicio 15: Conversor de Tiempo
# Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.

def convertirTiempo(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes
    

minutos = 145
horas, minutos_restantes = convertirTiempo(minutos)
print(f"{minutos} minutos son {horas} horas y {minutos_restantes} minutos.")