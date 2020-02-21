import sys
## Variables
nelementos = len(sys.argv)
suma = 0
media = 0
## Hacemos la suma de todos los elementos
#El elemento 0 lo saltamos
#pues es el nombre del script
#esto es una prueba
#esto es una prueba de alberto
try:
    for i in range(1, nelementos):
        suma += float(sys.argv[i])
    # y luego, con ella, la media
    media = float(suma / (nelementos - 1))
    ## Mostramos por pantalla los resultados
    print('El número de elementos introducidos es {}'.format(nelementos - 1))
    print('\nLa suma de todos los números es: {}'.format(suma))
    print('\nLa media de los números es: {}'.format(media))
except:
    print("Introduzca los parámetros correctamente")
