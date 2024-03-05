# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

from datetime import datetime

def calcAge(year):
    now = datetime.now()
    nowYear = now.year
    try:
        date_user = datetime.strptime(year, "%d/%m/%Y")
    except ValueError:
        date_user = datetime.strptime(year, "%d-%m-%Y")
    year = date_user.year
    age = nowYear - year
    print(f"Tienes {age} años.")

fecha_nacimiento = input("Introduce tu fecha de nacimiento: ")
calcAge(fecha_nacimiento)
    