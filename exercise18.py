# Ejercicio 18: Contador de Palabras
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

oracion = input("Escribe una oración: ")

palabras = oracion.split()

num_palabras = len(palabras)

print("El número de palabras en la oración es:", num_palabras)