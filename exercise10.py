# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
def determinar_dia(numero):
    for indice, dia in enumerate(dias):
        if indice + 1 == numero:
            return dia
            
resultado = determinar_dia(6)
print(resultado)
     