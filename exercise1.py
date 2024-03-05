# Ejercicio 1: Conversor de Temperatura
# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

def convert(value):
    result = 9 / 5 * value + 32
    return result
    
finalResult = convert(20)
print(finalResult)