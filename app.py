from mimetypes import init
from pathlib import *
from config import *
import os
from enum import Enum

#Escogido el tipo de partitura, saber en qué directorios buscar
def searchDirectory(tipo):
    list_dir = []
    if tipo == 'marcha' or tipo == 'marchas':
        list_dir.append(Path(DIR_MARCHAS))
    elif tipo == 'pasodoble' or tipo == 'pasodobles':
        list_dir.append(Path(DIR_PASODOBLES))
    elif tipo == 'obra' or tipo == 'obras':             
        list_dir.append(Path(DIR_OBRAS))             
    elif tipo == 'otra' or tipo == 'otras':         
        list_dir.append(Path(DIR_OTRAS))             
    else:             
        print('ERROR - NO EXISTE ESE TIPO DE PARTITURA')         
    return list_dir

#Dado el tipo de partitura y su nombre, buscar su ruta en los directorios
def searchSheet(list_dir, nombre):
    #Si solo se busca en un directorio
    rutaPartitura = ''
    if(len(list_dir) == 1):
        directorio = list_dir[0]
        directorio : Path
        for file in directorio.iterdir():
            if os.path.exists(file) and not(file.is_file()) and file.stem == nombre:
                print('OK- SE ENCONTRÓ LA PARTITURA ' + nombre)
                rutaPartitura = file
                break
            else:
                print('ERROR - NO SE ENCONTRÓ LA PARTITURA')
                break

    return  rutaPartitura

def getVoicesSheets(directory):   
    voicesSheet = []
    for x in directory.iterdir():
        if x.is_file():
            partitura = dict(
                nombre= x.stem,
                path = str(x)
            )
            voicesSheet.append(partitura)

    return voicesSheet


#funcion para convertir el nombre a "nombreMarchaNummeroDos"
def toCamelCase(name):
    s = name.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(name) == 0:
        return name
    return s[0].lower() + ''.join(i.capitalize() for i in s[1:])

#funcion para buscar el nombre dentro de la carpeta


if __name__ == "__main__":
    print('Introduzca el tipo de partitura:')
    tipo = input()
    list_dir = searchDirectory(toCamelCase(tipo))
    if(len(list_dir) == 1):
        print('Introduzca un nomnbre de marcha:')
        nombre = input()
        rutaPartitura = searchSheet(list_dir,toCamelCase(nombre))
        if(rutaPartitura):
            print('Introduzca la voz que desa buscar:')
            listaVoces = getVoicesSheets(rutaPartitura)
            for voz in listaVoces:
                print(voz['nombre'])
            

