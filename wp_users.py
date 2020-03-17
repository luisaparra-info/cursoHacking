# Supongamos la web del periódico New York Times, hecho en wordpress www.mytco.com
# Si ponemos las siguiente ruta: https://www.nytco.com/wp-json/wp/v2/users
# Nos devuelve un Json con info de los usuarios

import json
import urllib.request


def main():
    url = urllib.request.urlopen("https://www.nytco.com/wp-json/wp/v2/users")
    for u in json.loads(url.read()):
        id = u['id']
        name = u['name']
        user = u['slug']

        print("Id: {}\nNombre: {}\nSlug: {}\n".format(id, name, user))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
