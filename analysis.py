import json
import requests
import pandas as pd

# Solicitar al usuario una cadena para ser consultada
val = input('What is your request (type an string to be searched)?\n')

# Obtener de la fuente de datos todos los documentos que cumplan con el parametro entregado por el usuario

print()
print('... Buscando ...')
print()
response = requests.get("https://datos.gob.cl/api/3/action/package_search?q=" + val)
#print(response.json())

# Los datos obtenidos son del tipo requests.models.Response, asi que extraeremos los metadatos

jsondata = response.json()

# y luego, comenzamos a jugar con Pandas y los datos obtenidos

rawdf = pd.DataFrame.from_dict(jsondata)

rawdf.head()
