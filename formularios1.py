import mechanize
import argparse
from bs4 import BeautifulSoup

parse = argparse.ArgumentParser()
parse.add_argument("-b", "--buscar", help="Opción a buscar")
parse = parse.parse_args()


def main():
    if parse.buscar:
        # crea un navegador
        bus = mechanize.Browser()
        # No haga seguimiento del robot.txt
        bus.set_handle_robots(False)
        # No trate las cabecera http_equiv
        bus.set_handle_equiv(False)
        # Ponemos la cabecera de algún navegador
        bus.addheaders = [('User-agent', 'Safari')]
        bus.open("https://www.google.com")

        for n in bus.forms():
            print(n)

        # posición del formulario que va a recibir los datos
        bus.select_form(nr=0)
        bus['q'] = parse.buscar
        bus.submit()
        # print(bus.response().read())
        # vamos a parsearlo con bautifulsoup para que se vea mejor

        p = BeautifulSoup(bus.response().read(), 'html5lib')
        for link in p.find_all('a'):
            l = link.get('href')
            l = l.replace('/url?q=', '')
            print(l)





    else:
        print("Palabra a buscar")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo")
        exit()
