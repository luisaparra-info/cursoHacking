# Para obtener los temas tenemos que recorrer todos los enlaces del código fuente en el head que contienen la palabra "theme"
import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.nationalarchives.gov.uk"
    cabecera = {'User-Agent': 'Safari'}
    peticion = requests.get(url=url, headers=cabecera)
    soup = BeautifulSoup(peticion.text, 'html5lib')
    # buscamos en todas las etiquetas meta
    for l in soup.find_all('link'):
        if "wp-content/themes/" in l.get('href'):
            t = l.get('href')
            # creamos una lista con todos los elementos de la url teniendo como separador '/'
            t = t.split('/')
            pos = t.index('themes')
            # el nombre del tema es la posición siguiente a "themes"
            theme = t[pos + 1]
            print("Tema en uso: ", theme)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
