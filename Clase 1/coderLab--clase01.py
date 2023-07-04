# tipos de datos -----------------------------------------#
print (type(5))         #<class 'int'>
print(type(5.0))        #<class 'float'>
print(type(5j))         #<class 'complex'>
print(type("test"))     #<class 'str'>

# operaciones --------------------------------------------#
print(9/3)
print(9//3)
print(9%3)

# caracteres especiales ----------------------------------#
print("podemos usar \n en python para hacer un salto de linea") # salto de linea
print("podemos usar \t para agrega run tab en la linea")

print("podemos usar \ para imprimir un caracter especial \\t")
print(r"podemos usar r como prefijo al texto para imprimr un caracter especial \t")

print("""el uso de triple comilla 
permite escribir string 
en varias lineas""")

print("hola " + "mundo" + "!")  #concatenar

# variables ----------------------------------------------#
x = "hola mundo!"
print("x")