#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Transformador de imagenes para HOA
#Pablo Pizarro, 2014

#Importacion de librerias
import os
import sys

from PIL import Image  # @UnusedImport
import PIL


reload(sys)
sys.setdefaultencoding('UTF8') #@UndefinedVariable

#Definicion de constantes
ACTUAL_FOLDER = str(os.getcwd()).replace("\\","/")+"/"
VALID_FILES = ["gif","png","jpg","bmp","jpeg","ico"]

#Funciones
def consultArgument(argument,arguments): #funcion que consulta la existencia de un argumento
    for i in arguments:
        if i[0]==argument:
            return True
    return False #si no existe retorna falso

def consultParam(argument,arguments): #funcion que consulta el parametro de un argumento
    for i in arguments:
        if i[0]==argument: return i[1]
    return "%NULL%" #si no existe retorna null

#Consulto los archivos del directorio actual
archivos = os.listdir(ACTUAL_FOLDER)

#Variables a usar
archivos_validos = []
image_size = [0,0]

arguments = sys.argv #cargo los argumentos
arguments.append("end") #agrego final a la matriz de argumentos
arg = [] #matriz de argumentos
arg_p = [] #matriz parcial de argumentos
for k in range(1,len(arguments)-1): #se crea una matriz de argumentos
    if "-" in arguments[k]:
        arg_p.append(arguments[k].replace("-",""))
        if "-" not in arguments[k+1] and not "$" in arguments[k+1]:
            arg_p.append(arguments[k+1])
            if k!=len(arguments): k+=2
        else: arg_p.append("")
        arg.append(arg_p)
        arg_p = []
del(arguments)

#consulto los argumentos
#ayuda
if consultArgument("help",arg):
    print "Este script permite modificar las imagenes de una carpeta, transformandolas"+\
    "a un tamano deseado [alto x ancho] y cambiando su tonalidad, esta ideado para usarlo"+\
    "en el juego HOA, pero su uso es pubico dado que esta bajo la licencia GNU.\n"+\
    "Comandos:\n\t-help: Ayuda del script\n\t"+\
    "-fileformat %f :Escoger formato de trabajo [%f: formato]\n\t"+\
    "-to %f: Escoger formato final [%f: formato]\n\t"+\
    "-size %axh: Tamano de la imagen [%a=alto, %h=ancho]\n\t"+\
    "-filename %n :Nombre de los archivos a escoger [%n=nombre]\n\t\t  Si %n=%same% se mantiene el valor\n\t"+\
    "-count %c :Valor desde donde se comenzara a contar [%c=valor]\n\t"+\
    "-lower :Pasa los nombres a miniscula\n\t"+\
    "-upper :Pasa los nombres a mayuscula\n\t"+\
    "-silence: Ejecuta el script silenciosamente\n"

#si la ayuda no es cargada se ejecuta el script
else:

    #licencia
    if consultArgument("licence",arg): print "GNU"

    if len(archivos)>0: #si existen archivos
        if consultArgument("fileformat",arg): tipo = consultParam("fileformat",arg) #consulto el formato de imagen
        elif consultArgument("format",arg): tipo = consultParam("format",arg)
        else: tipo = raw_input("Ingrese el tipo de formato que quiere transformar: ").lower().strip().replace(".", "")
        if tipo in VALID_FILES: #si el formato es correcto
            for fil in archivos: #se recorren los archivos validos
                if tipo in fil: archivos_validos.append(fil)
            del(archivos)
            if len(archivos_validos)>0: #Si existen archivos tras el filtrado
                if consultArgument("to",arg): newTipe = consultParam("to",arg) #consulto por el tamano desado
                else: newTipe = raw_input("Ingrese el formato de salida: : ")
                if newTipe=="": newTipe = tipo #si no se ingreso nada el formato de salida es igual al de entrada
                if consultArgument("size",arg): size = consultParam("size",arg) #consulto por el tamano desado
                else: size = raw_input("Ingrese el tamano deseado [altoxancho]: ")
                if "x" in size: #si el tamaño es valido
                    size = size.split("x")
                    if size[0].isdigit() and size[1].isdigit(): #si el tamano es valido
                        image_size[0]=int(size[0]); image_size[1]=int(size[1])
                        if image_size[0]>0 and image_size[1]>0: #si son mayores a 0
                            if consultArgument("filename",arg): namefile = consultParam("filename",arg) #consulto el nombre a crear
                            else: namefile = raw_input("Ingrese el nombre de archivo a crear: ")
                            if len(namefile)>0:
                                if namefile=="%same%": keep = True
                                else: keep=False
                                if not keep:
                                    if consultArgument("count",arg): count = consultParam("count",arg) #consulto el nombre a crear
                                    else: count = raw_input("Ingrese el numero desde donde se comenzara a enumerar las imagenes: ")
                                else: count = "1"
                                if count.isdigit(): #si el contador es un numero
                                    number = int(count)
                                    #Cargo mas argumentos
                                    if consultArgument("lower",arg): lower = True
                                    else: lower = False
                                    if consultArgument("upper",arg): upper = True
                                    else: upper = False
                                    if consultArgument("silence",arg): silence = True
                                    else: silence = False
                                    for archivo in archivos_validos: #Se recorren los archivos validos
                                        try:
                                            if keep:
                                                pngfilename = archivo
                                                for res in VALID_FILES: pngfilename = pngfilename.replace("."+res,"")
                                                pngfilename+=".png"
                                            else: pngfilename = namefile+str(number)+"_0"+".png"
                                            if lower: pngfilename = pngfilename.lower()
                                            if upper: pngfilename = pngfilename.upper()
                                            imagen = Image.open(archivo)
                                            imagen.convert("RGBA")
                                            try: transfile = imagen.info["transparency"]
                                            except: pass
                                            layer = Image.new("RGBA", (image_size[0],image_size[1]))
                                            if tipo=="gif":
                                                try: imagen.resize((image_size[0],image_size[1]),PIL.Image.ANTIALIAS).save(pngfilename,transparency=transfile, quality=100)
                                                except: imagen.resize((image_size[0],image_size[1]),PIL.Image.ANTIALIAS).save(pngfilename,transparency=0, quality=100)
                                            else:
                                                try: imagen.resize((image_size[0],image_size[1]),PIL.Image.ANTIALIAS).save(pngfilename)
                                                except: raise IOError
                                            del(imagen)
                                            imagen = Image.open(pngfilename)
                                            try: transpng = imagen.info["transparency"]
                                            except: pass
                                            if keep:
                                                newimagefilename = archivo
                                                for res in VALID_FILES: newimagefilename = newimagefilename.replace("."+res,"")
                                                newimagefilename+="."+newTipe
                                            else: newimagefilename = namefile+str(number)+"_0"+"."+newTipe
                                            if lower: newimagefilename = newimagefilename.lower()
                                            if upper: newimagefilename = newimagefilename.upper()
                                            imagen.paste(imagen, layer)
                                            if newTipe=="gif":
                                                try: imagen.save(ACTUAL_FOLDER+newimagefilename,transparency=transpng, quality=100)
                                                except: imagen.save(ACTUAL_FOLDER+newimagefilename,transparency = 0, quality=100)
                                            else:
                                                try:imagen.save(ACTUAL_FOLDER+newimagefilename)
                                                except: raise IOError
                                            del(imagen)
                                            os.remove(ACTUAL_FOLDER+pngfilename)
                                            if not silence: print "Archivo '{0}' generado exitosamente".format(newimagefilename)
                                        except:
                                            print "Error :: Ocurrio un error al transformar la imagen '{0}'".format(archivo)
                                            print "Error :: Asegurese de que ningun programa este usando actualmente '{0}'".format(archivo)
                                        number+=1
                            else: print "Error :: Nombre de archivo no valido"
                        else: print "Error :: Tanto el ancho como el alto deben ser enteros mayores a cero"
                    else: print "Error :: El tamano debe ser un digito"
		      else: print "Error :: El tamano no es válido"
            else: print "Error :: Ningun archivo tiene el formato pedido"
        else: print "Error :: Formato de archivo no valido"
    else: print "Error :: No hay archivos en el actual directorio"