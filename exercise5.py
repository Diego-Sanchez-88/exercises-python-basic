# Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

def calc():
    arrNumbers = []
    i = 1
    while i <= 100:
        if i % 2 == 0:
            arrNumbers.append(i)
        i += 1 
    return arrNumbers
    
resultado = calc()
print(resultado)
