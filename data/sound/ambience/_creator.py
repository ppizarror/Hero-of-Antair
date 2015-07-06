#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Creador del fichero _textures.txt y _images.txt
#Pablo Pizarro, 2014

#Importación de librerias
import os
import sys


reload(sys)
sys.setdefaultencoding('UTF8') #@UndefinedVariable

#Definicion de constantes
ACTUAL_FOLDER = str(os.path.abspath(os.path.dirname(__file__))).replace("\\","/")+"/"
FILE_TEXTURES_NAME="_ambience_sounds.txt"
FOLDER_ITEM = "DATA_IMAGES_ITEMS"
VALID_FILE = "wav"

#Consulto los archivos del directorio actual
archivos = os.listdir(ACTUAL_FOLDER)

#Genero una matriz de archivos válidos
archivos_validos = []

#Recorro los archivos y genero una lista
for i in archivos:
    if VALID_FILE in i: archivos_validos.append(i)
del(archivos)

archivo = open(FILE_TEXTURES_NAME,"w")
archivo.write("-Sin sonido\n")
for j in archivos_validos:
    archivo.write(j+"\n")
archivo.close()