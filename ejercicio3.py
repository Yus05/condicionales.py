"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

numero_uno = int(input("Escribe un primer numero: "))

numero_dos = int(input("Escribe un segundo numero: "))

if numero_uno and numero_dos > 0:
    print(numero_uno/numero_dos)
elif numero_dos == 0:
    print("Error")
else:
    print(numero_uno/numero_dos)

    


