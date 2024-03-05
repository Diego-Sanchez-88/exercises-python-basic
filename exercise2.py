# Ejercicio 2: Calculadora de Propina
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.

def sumBill(order):
    total = 0
    for item in order:
        total += item
    return total
order = [1, 2, 3, 4, 5]
print(sumBill(order)) 
