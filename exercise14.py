# Ejercicio 14: Calculadora de Descuento
# Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

def aplicarDescuento(precio):
    precioFinal = precio - (precio * 0.20)
    return precioFinal

precioInicial = 20
precioConDescuento = aplicarDescuento(precioInicial)
print(precioConDescuento)