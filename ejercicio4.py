"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

Explicacion: https://www.freecodecamp.org/espanol/news/el-operador-del-modulo-python-que-significa-el-simbolo-de-porcentaje-en-python-resuelto/#:~:text=El%20s%C3%ADmbolo%20%25%20en%20Python%20se,de%20un%20problema%20de%20divisi%C3%B3n.
"""

numero = int(input("Escribe un numero entero: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Impar")

#EL OPERADOR MODULO, ME DEVUELVE EL RESIDUO DE LA DIVISION. SI EL RESIDUO ES CERO, ENTONCES EL NUMERO ES PAR. 



