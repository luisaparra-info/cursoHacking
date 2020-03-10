"""
"""
import requests
import argparse
from os import path

parser = argparse.ArgumentParser(description="Script subir archivo por POST")
parser.add_argument('-f', '--file', help="Indica el archivo a subir")
parser = parser.parse_args()


def main():
    if parser.file:
        if path.exists(parser.file):
            archivo = open(parser.file,'rb') #lectura como fichero binario
            headers ={'User-Agent':'Safari'}
            peticion = requests.post(url='https://curso--python-0-prueba-pentest.000webhostapp.com/',
                                     files={'uploaded_file':archivo},
                                     headers=headers)
            if parser.file in peticion.text:
                print(peticion.text)
                print("Archivo Subido con exito")
            else:
                print("Falló la subida del archivo")
        else:
            print("No existe el arcivo")
    else:
        print("Introduzca el archivo a subir")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
