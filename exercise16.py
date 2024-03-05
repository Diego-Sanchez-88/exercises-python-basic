# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

def mostrarNumeros(numeros):
    numeros = list(map(float, numeros.split(',')))
    # print(numeros)
    numerosPares = []
    numerosImpares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            numerosPares.append(int(numero))
        else:
            numerosImpares.append(int(numero))
    
    print(f'Los números pares son: {numerosPares}')
    print(f'Los números impares son: {numerosImpares}')
    
listaNumeros = input('Introduce una lista de numeros (separados por comas)')
mostrarNumeros(listaNumeros)