# sentencia IF


f = 3
h = 2
if (f == h):
    print('los numeros son iguales')
else:
    print('los numeros NO son iguales')

# IF anidado
num = int(input('escribe un numero'))

if num < 0: print(' numero negativo')
elif num == 0: print('el numero es 0')
elif num > 0: print('el numero es 4positivo')

# sentencia WHILE

print('While controlado por conteo')
print('===============================')
print('Sumador numero hasta 10')
sum=0
num=1
while (sum<=10):
  sum=num+sum
  num=num+1
  print('La suma es ' +str(sum))


print('While controlado con Evento')
print('===============================')
print('Calcular promedio')
promedio=0.1
total=0
contar=0
print('Escribe el valor (-1 para salir):')
grado=int(input())
while grado !=-1:
  total=total+grado
  contar= contar + 1
  print('Escribe el valor (-1 para salir):')
  grado=int(input())
  promedio=total/contar
  print('El promedio es ' +str(promedio))

print('While con sentencia break')
print('===============================')
print('Sumador numero hasta 20')
sum=0
num=0
while (sum<=30):
 sum=num+sum
 num=num+1
 print('El num es ' +str(num))
 if num > 4:
   break
print('La suma es ' +str(sum) + ' y no ha llegado a 30 por el break')

print('While con sentencia continue')
print('===============================')
vari=10
while (vari>0):
  vari=vari-1
  if vari== 4:
    print('entra en el continue y la vari es ' +str(vari))
  continue
print('La vari es ' +str(vari))

print('for con listas')
print('===============================')
nombre_list=['paco','manu','alonso']
for nombre in nombre_list:
  print('Su nombre es: ', nombre, ' el numero de letras son:', len(nombre))

a=[1, 2, 3, 4 ,5]
for i in a:
    print('el bucle va por el numero: ',i, 'y la longitud de la lista es: ',len(a))

print('for con tuplas')
print('===============================')
tupla_list=['paco','48989642','madrid','encargado']
for tupla in tupla_list:
  print(tupla)