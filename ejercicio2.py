"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contrasena = "CaRacas12"
contrasena = contrasena.lower()

pregunta = input("Escribe la contrasena: ")
pregunta = pregunta.lower()

if pregunta == contrasena:
    print("Contrasena valida.")
else:
    print("Contrasena incorrecta.")

    
