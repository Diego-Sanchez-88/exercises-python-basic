# Ejercicio 17: Conversor de Millas a Kilómetros
# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

def convertir(millas):
    km = 1.60934
    kilometros = millas * km
    return kilometros
    
resultado = convertir(20)
print(resultado)