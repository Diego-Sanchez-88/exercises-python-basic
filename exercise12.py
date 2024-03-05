# Ejercicio 12: Calculadora de Área de un Rectángulo
# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.

def calcularArea(params):
    longitud, ancho = map(float, params.split(','))
    area = longitud * ancho
    print(f'El área del triángulo es {area} cm.')
    
    
parametros = input("Introduce una longitud y un ancho (en cm) separados por una coma: ")
calcularArea(parametros)