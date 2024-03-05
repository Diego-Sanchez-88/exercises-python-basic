# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")  
    return palabra == palabra[::-1]

palabra_usuario = input("Ingresa una palabra: ")
# Palabras: salud, salas

if es_palindromo(palabra_usuario):
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")