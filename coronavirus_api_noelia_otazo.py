import json
from pathlib import Path

import requests
import os

#La dirección de la API es: https://api.covid19api.com/
try:        
    def 


    while True:
        #borrar la pantalla Para DOS/Windows
        os.system ("cls") 
        print("Gestión de datos de municipios de Castilla y León")
        print("1. ")
        print("2. Busqueda de municipios mediante provincia.")
        print("3. Busqueda de provincia y población mediante municipio.")
        print("4. Busqueda de municipios mediante Mancomunidad.")
        print("5. Enumeración de municipios mediante provincia.")
        print("6. Busqueda de municipios por numero de habitantes.")
        print("7. Lista de municipios por nombre y numero de habitantes")
        print("8. Salir")
        opcion = int(input())
        
        if opcion==1:
            print("bip bip")
        elif opcion==2:
            print("bip bip")
        elif opcion==3:
            print("bip bip")
        elif opcion==4:
            print("bip bip")
        elif opcion==5:
            break
 
        input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")