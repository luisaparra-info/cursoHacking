import string

archivo = open("archivo1.txt", "w")
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
pais = input("Escribe tu pais: ")

archivo.write(nombre + "\n"+edad + "\n"+pais + "\n")

print("Se ha escrito el fichero correctamente")

archivo.close()
""""
archivo = open("archivo1.txt","r")
lista = archivo
for linea in lista
    print (linea)
"""