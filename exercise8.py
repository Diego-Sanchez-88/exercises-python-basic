# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

# IMC = peso (kg) / [estatura (m)]2
def calcIMC(peso, estatura_cm):
    estatura_m = estatura_cm / 100
    return peso / (estatura_m ** 2)

resultado = calcIMC(75, 175)
print(resultado)