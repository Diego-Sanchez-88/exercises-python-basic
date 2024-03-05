# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el usuario.

def sumNums(listNums):
    result = 0
    for num in listNums:
        result += int(num)
    print(result)
    
    
user_nums = [int(x) for x in input('Introduce números separados por comas: ').split(',')]
sumNums(user_nums)