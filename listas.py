# LISTAS

frutas = ["manzana",1+1,"limon"]

print(frutas[0])
print(frutas[1])
print(frutas[2])


print(frutas[-1])
print(frutas[-2])
print(frutas[-3])


numeros = [0,1,2,3,4,5,6,7,8,9]

pos_2_al_6 = numeros[2:3]
print(pos_2_al_6)
pos_mayor_4 = numeros[5:]
print(pos_mayor_4)

pares=numeros[::2]
impares=numeros[1::2]
print(pares)
print(impares)
print(4 in numeros)
print(12 in numeros)

# Ejemplo de una lista. Pilotos oficiales de Ferrari en 2014.
Ferrari2014=["Fernando Alonso", "Kimi Raikkonen"]
#print (Ferrari2014)
# Ejemplo de otra lista. Pilotos oficiales de Ferrari en 2013.
Ferrari2013=["Fernando Alonso", "Felipe Massa"]
#print (Ferrari2013)
#print(Ferrari2014[1])

# pop: Extraemos a Kimi (que está en la posición número 1) de la lista. Alonso está en la posición 0.
nombre = Ferrari2014.pop(1)
print(nombre)
print(Ferrari2014)

# append: Añadimos a Kimi al final de la lista
Ferrari2014.append("Kimi Raikkonen")
print (Ferrari2014)

# del:Eliminamos el elemento de la primera posición de la lista (Fernando)
del(Ferrari2014[0])

# insert: Añadimos a Fernando en la primera posición
Ferrari2014.insert(0, "Fernando Alonso")
print (Ferrari2014)

# extend: Juntamos los pilotos del 2013 y los del 2014. Fernando estará repetido.
Ferrari2014.extend(Ferrari2013)
print (Ferrari2014)

#remove: Borramos la primera vez que aparece Fernando Alonso
Ferrari2014.remove("Fernando Alonso")
print (Ferrari2014)
