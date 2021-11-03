# coding=utf-8
# Creador del fichero _textures.txt y _images.txt
# Pablo Pizarro, 2014

# Importación de librerias
import os
import sys

reload(sys)
sys.setdefaultencoding('UTF8')  # @UndefinedVariable

# Definicion de constantes
ACTUAL_FOLDER = str(os.getcwd()).replace("\\", "/") + "/"
DELETE = ["_16", "_32"]
FILE_TEXTURES_NAME = "_textures.txt"
FILE_PASTE_NAME = "_paste.txt"
FILE_PASTE_COM = "#Items\n"
FOLDER_ITEM = "DATA_IMAGES_ITEMS"
RESTRICTED = ["vacio", "no_lw", "no_rw", "no_casco", "no_pantalon", "no_chaleco", "no_botas"]
VALID_FILE = "gif"

# Consulto los archivos del directorio actual
archivos = os.listdir(ACTUAL_FOLDER)

# borro los string en DELETE
for k in range(len(archivos)):
    archivos[k] = str(archivos[k]).replace(DELETE[0], "").replace(DELETE[1], "")

# archivos validos
archivos_validos = []

# recorro los archivos y voy agregando a archivos_validos
for k in range(len(archivos)):
    if VALID_FILE in archivos[k] and archivos[k].replace(".gif", "") not in archivos_validos: archivos_validos.append(
        archivos[k].replace(".gif", ""))

# ordeno la matriz
archivos_validos.sort()

# elimino los archivos restringidos
for r in RESTRICTED:
    try:
        archivos_validos.remove(r)
    except:
        pass

# genero un archivo de texto
archivo = open(FILE_TEXTURES_NAME, "w")
for i in archivos_validos:
    archivo.write(i + "\n")
archivo.close()  # cierro el archivo

# Consulto nuevamente los archivos del directorio actual
archivos = os.listdir(ACTUAL_FOLDER)

# matriz de links para self.images en HOA
links = []

# recorro los archivos y verifico si es una imagen
for fil in archivos:
    if VALID_FILE in fil:
        links.append(
            "\t\t\"" + fil.replace("." + VALID_FILE, "") + "\":PhotoImage(file=" + FOLDER_ITEM + "+\"" + fil + "\"),\\")

# agrego imagenes no validas
links.append(
    "\t\t\"vacio_16\":PhotoImage(data=\"R0lGODlhEAAQAIAAAP///wAAACH5BAEAAAEALAAAAAAQABAAAAIOjI+py+0Po5y02ouzPgUAOw==\"),\\")

# ordeno la matriz
links.sort()

# inserto comentario
links.insert(0, FILE_PASTE_COM)

archivo2 = open(FILE_PASTE_NAME, "w")
for i in links:
    archivo2.write(i + "\n")
archivo2.close()
