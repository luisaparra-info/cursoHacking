import requests
import argparse

# Definimos la descripción de nuestro programa
parser = argparse.ArgumentParser(description="Detector de cabeceras")

# Vamos añadiendo parámetros a nuestro programa
# La opción extendida en este caso "tarjet" para a ser la variable que contiene el valor del parámetro
parser.add_argument('-t', '--target', help="Objetivo")

# Hemos terminado de definir los argumentos y queremos que estén disponibles
parser = parser.parse_args()

# Prubamos a ejecutar en el terminal
# cabeceras.py -t y cabeceras.py -h

def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            cabeceras = dict(url.headers)
            for cabecera in cabeceras:
                print(cabecera +" : " + cabeceras[cabecera])

        except Exception as err:
            print("No se pudo conectar con " + str(err))


if __name__ == '__main__':
    main()
