# Este script se utilizan cosas muy interesantes, por una parte estamos leyendo de un fichero un listado de plugins
# y por otra parte estamos usando una librería para representar una barra de progreso,
# este fichero difiere un poco al original del curso porque lo he tenido que adaptar a python3
import requests
from os import path
from bar import Bar

def main():
	if path.exists("wp_plugins.txt"):
		w = open("wp_plugins.txt",'r')
		#w=lista de todos los plugins del fichero
		w = w.read().split('\n')
		#lista=lista de los plugins encontrados
		lista = []
		url = "https://www.nationalarchives.gov.uk"
		with  Bar("Espere...",count=len(w)) as b:

			for plugin in w:
				b.step()
				try:
					p = requests.get(url=url+"/"+plugin)
					# si la url formada existe
					if p.status_code == 200:
						final = url+"/"+plugin
						lista.append(final.split("/")[-2])
				except:
					pass
			b.exit()
		for plugin in lista:
			print("Plugin encontrado: {}".format(plugin))

	else:
		print("No se encuentra la lista")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()