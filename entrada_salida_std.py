###############################
#    ENTRADA ESTANDAR         #
###############################
nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
print("Hola {}, tu edad es {} y el doble de tu edad es {}. ".format(nombre, edad, edad * 2))

# Control de exceciones en la entrada de datos
def read_int(msg):
    try:
        return int(input(msg))
    except:
        return read_int('El dato introducido no es correcto, vuelva a intentarlo \n> ')


def multi_read():
    data = []
    n = read_int('¿Cuantos valores quiere leer? \n> ')
    for i in range(n):
        data.append(input("Introduce un valor: "))

    return data


print(multi_read())

#ver entrada_parametros.py

###############################
#    SALIDA  ESTANDAR         #
###############################
# sustituye en valor /n por el valor que especifiquemos
for i in range(5):
    print(i, end='')

print("Cuesta", 3, "euros")
try:
    print("Cuesta " + 3 + " euros")
except:
    print("Cuesta " + str(3) + " euros")

#Trabajo con variables
saludo = "Hola"
lugar = "Mundo"
print('\n{} {}'.format(saludo, lugar))
##Indicando la posición del elemento
print('\n{1} {0}'.format(saludo, lugar))
##Indicando, además, el número de caracteres que ocupa cada string
####(10 primero, 8 segundo).
print('{0:10s} {1:8s}'.format(saludo, lugar))

# Formatos

# s	Cadena
# d	Entero
# o	Octal
# x	Hexadecimal
# f	Real

from math import pi
print('Pi con cuatro decimales: {0:.4f}'.format(pi))

for x in range(1,11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(4))

#Crear una tabla de enteros (d)
for x in range(1,11):
    print('{0:2d} {1:4d} {2:4d}'.format(x, x * x, x * x * x))
    #Indicamos el tipo de elemento y el número de caracteres

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(7))
################################
#00012
#-003.14
#3.14159265359 (El número es mayor)

tabla = {'Pepe': 5.5, 'Andrea': 7.25, 'Juan': 6}

for nombre, nota in tabla.items():
    print('{0:7} ==> {1:2.2f}'.format(nombre, nota))