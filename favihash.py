# BIENVENIDO A FAVIHASH!
# by TheMast3rs
# Leer archivo "Readme.md" antes de usar

#Importar librerias
import mmh3,requests,codecs,argparse

#Parametro -u URL
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Direccion URL")
args = parser.parse_args()
url = args.url
#Banner
Banner ="""
██████║██████║██║  ██║██████║██║ ██║██████║██████║  ██  ██║ 
██║    ██╔═██║██║  ██║  ██║  ██║ ██║██╔═██║███║   ██████████║
█████║ ██████║██║  ██║  ██║  ██████║██████║██████║  ██╔═██║
██║    ██╔═██║ ██ ██╔╝  ██║  ██╔═██║██║ ██║  ║███║██████████║
██║    ██║ ██║  ███╔╝ ██████╗██║ ██║██║ ██║██████║  ██║ ██║
╚═╝    ╚═╝ ╚═╝  ╚══╝  ╚═════╝╚═╝ ╚═╝╚═╝ ╚═╝╚═════╝  ╚═╝ ╚═╝
--------------------------------------------->> FAVICON HASHER
--------------------------------------------->> By TheMast3rs 
"""
print(Banner)
#Funcionamiento
def favihash():
	response = requests.get(url+'/favicon.ico')                     #Obtener URL
	favicon = codecs.encode(response.content,"base64")              #Codificar URL base64
	hash = mmh3.hash(favicon)                                       #Codificar hash mmh3
	print("[URL        ]: ", url)                                   #Mostrar URL
	print("[HASH       ]: ", hash)                                  #Mostrar hash
	print("[SHODAN DORK]: ", "http.favicon.hash:"+str(hash))        #Mostrar Shodan Dork

try:
	res = requests.get(url+'/favicon.ico', timeout=30)
	favihash()
except requests.exceptions.MissingSchema as e:
	print("ERROR: La URL no posee FAVICON o no existe, por favor verifique la URL")
except requests.ConnectionError as e:
        print("ERROR: La URL no posee FAVICON o no existe, por favor verifique la URL")
