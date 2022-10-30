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
                rutaPartitura = file
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

def getVoicesOptions(type, name):
    list_dir = searchDirectory(toCamelCase(type))
    list_voices = []
    if(len(list_dir) == 1):
        route = searchSheet(list_dir,toCamelCase(name))
        if(route):
            list_voices = getVoicesSheets(route)
    return list_voices

def getVoice(type, name, voice):
    listaVoces = getVoicesOptions(type,name)
    if(listaVoces):
        for voz in listaVoces:
            if(voz['nombre'] == voice):
                return voz
    

if __name__ == "__main__":
    
    listaVoces = getVoicesOptions('marcha','La estrella erwerwer')

    if(listaVoces):
        for voz in listaVoces:
            print(voz['nombre'] + ':'+voz['path'])
    else:
        print('No encontrado')

    voz = getVoice('marcha','La estrella sublime','trompeta1')
    print(voz)

