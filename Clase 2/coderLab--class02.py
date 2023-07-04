
#ingreso de datos
print("comienza el programa")

nombre = input("ingrese nombre: ")
edad = input("ingrese su edad: ")

print("hola " + nombre + " el proximo año tendras " + str(int(edad)+1) )

#imprimir una posicion del string
"""
H O L A _ M U N D O !
0 1 2 3 4 5 6 7 8 9 10
"""
frase = "Hola Mundo!"
print(frase[2])         #imprime O
print(frase[-2])        #imprime O
print(frase[2:6])       #imprime LA M
print(frase[6:1:-2])    #imprime desde la pos6 hasta las pos1 de 2n2    U L
print(frase[2:])        #imprime desde la pos2 hasta el final           OLA MUNDO!
print(frase[::-1])      #imprime la variable al reves                   !ODNUM ALOH

"""
las listas se pueden trabajar como las variables
son mutables
"""

"""
las tuplas son colecciones de datos tambien se puede trabajar como las variables o listas
pero son inmitables, no se puede modificar
"""