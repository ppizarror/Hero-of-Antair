# coding=utf-8
"""
CONFIG
Maneja las configuraciones del núcleo de HOA.

Autor: PABLO PIZARRO @ ppizarror
Fecha: JULIO 2015, 2017
Licencia: GPLv2
"""

# Importación de librerías
import os
from errors import *

# Constantes
_bindir = "bin"
_actualpath = str(os.path.abspath(
    os.path.dirname(__file__))).replace(_bindir, "")
CONFIG_FOLDER = _actualpath + "config/"
CONFIG_HOA_FILE = "hoa.configs"


def getConfigValue(configFile, upper=False, autoTrue=True):
    """Lee la linea de un archivo de configuracion"""
    try:
        f = open(CONFIG_FOLDER + configFile, "r")
    except:
        st_error("Configuracion --{0} no definida".format(configFile), True)
    line = f.readline().strip()
    # Se comprueba si el valor es booleano
    if autoTrue and (line == "1" or line == "True" or line == "TRUE"):
        return True
    elif autoTrue and (line == "0" or line == "False" or line == "FALSE"):
        return False
    # Si no es booleano
    else:
        if upper:
            return line.upper()
        return line


def loadConfigFile(configFile):
    """Retorna todo el contenido de un archivo de configuraciones"""
    f = open(CONFIG_FOLDER + configFile, "r")
    content = ""
    for line in f:
        content += line
    f.close()
    return content


def addLineConfigFile(configFile, line):
    """Añade una linea a un archivo de configuraciones"""
    content = loadConfigFile(configFile)
    f = open(CONFIG_FOLDER + configFile, "w")
    f.write(content)
    if line not in content:
        f.write("\n" + line)
    f.close()


def setConfig(configFile, configValue):
    """Crea un archivo de configuracion con el valor configValue"""
    try:
        f = open(CONFIG_FOLDER + configFile, "w")
    except:
        st_error("Error al escribir en el archivo {0}".format(
            configFile), True)
    f.write(configValue)
    f.flush()
    f.close()
