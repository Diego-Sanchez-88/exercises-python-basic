# Ejercicio 3: Verificación de Edad
# Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.

def checkAge(age):
    if age >= 18:
        message = 'Es mayor de edad'
    else: 
        message = 'No es mayor de edad'
    return message

# ageToCheck = 20
ageToCheck = 5

result = checkAge(ageToCheck)
print(result)