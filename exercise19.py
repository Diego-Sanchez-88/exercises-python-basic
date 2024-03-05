# Ejercicio 19: Verificación de Año Bisiesto
# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.

def checkYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Introduce un año: "))

if checkYear(year):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es un año bisiesto.")