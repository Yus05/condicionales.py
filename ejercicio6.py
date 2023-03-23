"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

Grupo A -> Mujeres con nombre anterior a la M / Hombres con nombre posterior a la N.

Grupo B -> Mujeres con nombre posterior a la N / Hombres con nombre anterior a la M.
 
"""
tupla_1 = ("a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")

tupla_2 = ("n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

sexo_1 = "Mujer"
sexo_1 = sexo_1.lower()

sexo_2 = "Hombre"
sexo_2 = sexo_2.lower()

nombre = input("Escribe tu nombre: ")
nombre = nombre.lower()
nombre = nombre[0]

sexo = input("Eres hombre o mujer: ")

if nombre in tupla_1 and sexo in sexo_1:
    print("Eres del grupo A")
elif nombre in tupla_2 and sexo in sexo_2:
    print("Eres del grupo A")
elif nombre in tupla_2 and sexo in sexo_1:
    print("Eres del grupo B")
elif nombre in tupla_1 and sexo in sexo_2:
    print("Eres del grupo B")















