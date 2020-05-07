import json
from pathlib import Path

import requests
import os

#La dirección de la API es: https://api.covid19api.com/
try:        
    def sumario():
        api_address="https://api.covid19api.com/summary"
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            print(type(json_data))
            print(json_data)

        input("Presione una tecla para continuar...")    

    def datos_pais():
        api_address="https://api.covid19api.com/countries"
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            print(type(json_data))
            print(json_data)

        input("Presione una tecla para continuar...")  



    while True:
        #borrar la pantalla Para DOS/Windows
        os.system ("cls") 
        print("Covid-19")
        print("1. Sumario de casos actualizado diariamente.")
        print("2. Datos por País.")
        print("3. Busqueda de provincia y población mediante municipio.")
        print("4. Busqueda de municipios mediante Mancomunidad.")
        print("5. Enumeración de municipios mediante provincia.")
        print("6. Busqueda de municipios por numero de habitantes.")
        print("7. Lista de municipios por nombre y numero de habitantes")
        print("8. Salir")
        opcion = int(input())
        
        if opcion==1:
            sumario()

        elif opcion==2:
            datos_pais()1

        elif opcion==3:
            print("bip bip")

        elif opcion==4:
            print("bip bip")

        elif opcion==5:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")