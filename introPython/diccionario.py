# DICCIONARIOS

usuario = {
    'nombre': 'Nombre del usuario',
    'edad' : 23,
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'notas' : []
}

print (usuario.keys())
print (usuario.values())
print(usuario.get("skills").get("programacion"))

notas = usuario.get('notas', [])
if notas:
    media=0
    for nota in notas:
        media=media+nota
    media=media/len(notas)
    print(round(media,2))
else:
    print("No tiene notas")


usuarios = [ 'Eduardo', 'Fernando', 'Uriel', 'Rafael']
diccionario = { usuario:position + 1 for position, usuario in enumerate(usuarios)  }

print(diccionario)
diccionario = {'Piloto 1':'Fernando Alonso', 'Piloto 2':'Kimi Raikkonen', 'Piloto 3':'Felipe Massa'}
print(diccionario)
# get(): Devuelve el valor que corresponde con la key introducida.
print(diccionario.get('Piloto 1'))

# pop(): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(diccionario.pop('Piloto 1'))
print(diccionario)

# update(): Actualiza el valor de una determinada key o lo crea si no existe.
diccionario.update({'Piloto 4':'Lewis Hamilton'})
diccionario.update({'Piloto 2':'Sebastian Vettel'})
print(diccionario)

# "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print ("Piloto 1" in diccionario)

# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
print ("Sebastian Vettel" in diccionario.values())

# del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
del diccionario['Piloto 2']
print(diccionario)
