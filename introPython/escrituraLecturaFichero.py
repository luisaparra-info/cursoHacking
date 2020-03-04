import string
from io import open
# Escritura en un fichero
texto = "Una línea con texto\nOtra línea con texto\nOtra línea más abajo del todo"

fichero=open('archivo1.txt','w') # fichero.txt ruta donde lo crearemos, w indica modo de escritura, write (puntero principio)

fichero.write(texto) # Escribimos dentro del fichero el contenido de la variable texto

fichero.close() # Cuando dejamos de trabajar, cerramos el fichero siempre

# Lectura de un fichero completo
fichero = open('archivo1.txt','r') # Ya tenemos el fichero abierto

texto = fichero.read() # Almacenamos el contenido existente en el fichero en la variable texto

fichero.close()

print(texto)

# Intrudicir línea a línea en una lista

fichero = open('archivo1.txt','r') # Ya tenemos el fichero abierto

lineas = fichero.readlines()

fichero.close()

print(lineas)
print(lineas[-1])

# Añadir más contenido a un fichero de texto:

fichero = open('archivo1.txt','a') # modo append y el puntero se coloca al final

fichero.write('\nCuarta línea del fichero')

fichero.close()

# Lectura línea por línea de forma secuencial

with open('archivo1.txt','r') as fichero:

    for linea in fichero:

        print(linea)
fichero.close()

# Puntero lectura / escritura

fichero = open('archivo1.txt','r') # Ya tenemos el fichero abierto

fichero.seek(0) # Puntero al principio
fichero.read(10) # Leemos 10 caracteres

fichero.read(10) # Leemos 10 caracteres más, a partir del 10 donde está el puntero

fichero.seek(0)
fichero.seek( len(fichero.readline()) ) # Leemos la primera línea y situamos el puntero al principio de la segunda
fichero.read() # Leemos  lo que queda del puntero hasta el final
fichero.close()

fichero = open('archivo1.txt','r+') # Ya tenemos el fichero abierto

lineas = fichero.readlines()
lineas[2] = "Esta línea se ha modificado en memoria\n" # Modificar la linea 3

fichero.seek(0) # Colocar el puntero al comienzo

fichero.writelines(lineas) # Escribimos la lista de lineas

fichero.close()

