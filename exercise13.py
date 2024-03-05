# Ejercicio 13: Verificación de Número Primo
# Escribe un programa que determine si un número ingresado por el usuario es primo o no.

def checkNumber(number):
    number = int(number)
    if number < 2:
        result = False
    else:
        result = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                result = False
                break

    if result:
        print('El número introducido sí es primo.')
    else:
        print('El número introducido no es primo.')

number = input("Introduce un número para comprobar si es primo o no: ")
checkNumber(number)