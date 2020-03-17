# Si revisamos el código fuente de una web en wordpress vemos que hay una etiqueta que nos da la versión
# esta etiqueta para el sitio: https://jquery.com
# sería : <meta name="generator" content="WordPress 4.5.2">

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://jquery.com"
    cabecera = {'User-Agent':'Safari'}
    peticion = requests.get(url=url, headers=cabecera)
    soup = BeautifulSoup(peticion.text, 'html5lib')
    #buscamos en todas las etiquetas meta
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            version = v.get('content')
            print(version)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()