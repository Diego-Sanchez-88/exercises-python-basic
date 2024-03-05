# Ejercicio 7: Calculadora Simple
# Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.


def calc(operation, numbers):
    result = 0
    if operation == 'sumar':
        for number in numbers:
            result += number
    elif operation == 'restar':
        for number in numbers:
            result -= number
    elif operation == 'multiplicar':
        result = 1
        for number in numbers:
            result *= number
    elif operation == 'dividir':
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
    return result

operation = 'sumar'
numbers = [2, 5]
resultado = calc(operation, numbers)
print(resultado)
