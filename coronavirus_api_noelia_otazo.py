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
        print("3. .")
        print("4. Salir")
        opcion = int(input())
        
        if opcion==1:
            sumario()

        elif opcion==2:
            datos_pais()

        elif opcion==3:
            print("bip bip")

        elif opcion==4:
            print("bip bip")

        elif opcion==5:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")