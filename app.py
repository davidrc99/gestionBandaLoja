from mimetypes import init
from pathlib import *
from config import *
import os

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
        list_dir.append(Path(DIR_MARCHAS))
        list_dir.append(Path(DIR_PASODOBLES))
        list_dir.append(Path(DIR_OBRAS))
        list_dir.append(Path(DIR_OTRAS))
    return list_dir

#Dado el tipo de partitura y su nombre, buscar su ruta en los directorios
def searchSheet(list_dir, nombre):
    #Si solo se busca en un directorio
    rutaPartitura = ''
    print(list_dir)
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
                rutaPartitura = 'ERROR'
    else:
        for dir in list_dir:
            list_dir_aux = []
            list_dir_aux.append(dir)
            searchSheet(dir,nombre)

    return  rutaPartitura    

#funcion para convertir el nombre a "nombreMarchaNummeroDos"
def toCamelCase(name):
    s = name.replace("-", " ").replace("_", " ")
    s = s.split()
    if len(name) == 0:
        return name
    return s[0].lower() + ''.join(i.capitalize() for i in s[1:])

#funcion para buscar el nombre dentro de la carpeta




def searching_all_files(directory: Path):   
    file_list = [] # A list for storing files existing in directories

    for x in directory.iterdir():
        if x.is_file():
           file_list.append(x)
        else:

           file_list.append(searching_all_files(directory/x))

    return file_list


p = Path(DIR_RAIZ)

# for file in Path(DIR_RAIZ):
#     if file.is_file():


if __name__ == "__main__":
    print('Introduzca el tipo de partitura:')
    tipo = input()
    print('Introduzca un nomnbre de marcha:')
    nombre = input()

    list_dir = searchDirectory(toCamelCase(tipo))

    print(searchSheet(list_dir,toCamelCase(nombre)))



