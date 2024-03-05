# Ejercicio 9: Conversor de Divisas
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

def calc(amount):
    amountRes = amount * 0.85
    return amountRes

resultado = calc(8)
print(resultado)