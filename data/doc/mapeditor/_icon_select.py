#Creador de iconos
#Usar para hoa
#Pablo Pizarro - 2014

#Importacion de librerias
import os
import shutil
import sys

import Win32IconImagePlugin  # @UnusedImport @UnresolvedImport


ACTUAL_PATH = str(os.getcwd()) #Definicion del directorio actual
ICON_FORMAT = ".ico"
ICON = "ico"
PATH_SCRIPTS = ACTUAL_PATH.replace("\\images\\items","\\scripts") #Directorio de scripts
PATH_SCRIPTS_MAGICK = ACTUAL_PATH.replace("\\images\\items","\\pythonmagick\\PythonMagick") #Directorio de scripts
PATH_ICON_NORMAL = ACTUAL_PATH.replace("\\images\\items","\\icons") #Directorio de iconos normal
PATH_ICON_SELF = ACTUAL_PATH+"\\_icons" #Carpeta actual de iconos
VALID_FILES = "_16" #archivos con terminacion valida
VALID_FILEFORMAT = ".gif" #formato a usar
VALID_FILES+=VALID_FILEFORMAT

#Importacion de nuevas librerias defindias en path
sys.path.append(PATH_SCRIPTS_MAGICK)
sys.path.append(PATH_SCRIPTS)

#Importo las librerias para poder trabajar en iconos

#Consulto los archivos del directorio actual
archivos = os.listdir(ACTUAL_PATH)

#Matriz de archivos validos
archivos_validos = []

#Recorro los archivos, si es valido se agrega
for arch in archivos:
    if VALID_FILES in arch: archivos_validos.append(arch)
del (archivos)

#Recorro los archivos validos y los convierto a un icono
for im in archivos_validos:
    shutil.copy(im, "_icons")
    
try: os.remove(ACTUAL_PATH+"\\_icon_select.pyc")
except: pass