import requests
import json
from rich import print

url = "https://remax.com.mx/map/FetchMapData"

payload = {
    "moneda": "MXN",
    "locationKeyword": "ciudad de mexico, ciudad de mexico",
    "ciudad_id": "10243",
    "operacion": "1",
}

headers = {
   'Accept': '*/*',
  'Accept-Language': 'es-419,es;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': '_gcl_au=1.1.1197707427.1738331239; _fbp=fb.2.1738331239006.986851811560217439; _hjSessionUser_3542741=eyJpZCI6IjkzZjU4MWY5LTBhMGYtNWVkOS1hYzY2LWY3ZTE3MTBlYTI4YyIsImNyZWF0ZWQiOjE3MzgzMzEyMzk1NDEsImV4aXN0aW5nIjp0cnVlfQ==; _tac=false~self|not-available; _ta=mx~1~8dbc7739cfa9ad54729fa24447ee2d06; _gid=GA1.3.901592234.1738604665; _hjSession_3542741=eyJpZCI6ImZlOWQ3OTY1LTJlMDUtNGU3My05NWYzLTE3NDI2YjI1MDRlZCIsImMiOjE3Mzg2MTc2NTA1NzAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; remaxsession=840d19d6e9d64b8635c660200f20047db61af00a; _gat_UA-2876860-1=1; _ga_T5EMC56PR7=GS1.1.1738617650.3.1.1738619385.59.0.0; _ga=GA1.3.943897412.1738331239; remaxsession=d633ea214b5fb8977f9f2c226e4b5d47ded99c37',
  'Origin': 'https://remax.com.mx',
  'Referer': 'https://remax.com.mx/propiedades/ciudad+de+mexico_ciudad+de+mexico/venta',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.post(url, headers=headers, json=payload)

# Convertir el JSON de la respuesta en un diccionario
json_data = json.loads(response.text)["data"]["prop_data"]


array=[]
for data in json_data:
  array.append({
    'colonia_nombre':data['colonia_nombre'],
    'estado_nombre':data['estado_nombre'],
    'ciudad_nombre':data['ciudad_nombre']
    })


print(array)


# OTRA FORMA DE REALIZAR

# response = requests.post(url, json=payload, headers=headers)

# if response.status_code == 200:
#     data = response.json()  # Convertimos la respuesta a JSON
#     primer_elemento = data.get("data", {}).get("prop_data", [])[0]  # Obtenemos el primer elemento de la lista
    
#     print(primer_elemento)  # Mostramos el primer elemento
# else:
#     print(f"Error en la solicitud: {response.status_code}")