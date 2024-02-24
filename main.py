#clase principal que se encarga de crear un objeto de tipo carpeta que se solicita la ruta por consola
# y luego se crea una lista con los archivos que se encuentran en la carpeta
# y se crea un objeto de tipo archivo por cada archivo en la lista
# y se leen los archivos y se cuentan las palabras que se repiten
# y se imprime el resultado
from carpeta import carpeta
import os

#solicita palabra a buscar
#palabra = input("Ingrese la palabra a buscar: ")
#Recibe ruta
#ruta = input("Ingrese la ruta de la carpeta donde buscara: ")

palabra = "hola"
ruta = "C:\pruebas\pruebas2"

#Crea objeto carpeta si encuentra la ruta si no muestra mensaje
if os.path.exists(ruta):
    folder =  carpeta(ruta, palabra)
    print("CARPETA "+ ruta +" ENCONTRADA")
    #Busca archivos en la carpeta
    folder.buscarArchivos()
else:
    print("CARPETA NO ENCONTRADA")
    exit()

#si encontro archivos crea objetos archivo y los guarda en la lista de archivos de la carpeta
if len(folder.getLstrutas()) > 0:
    folder.crearArchivos()

#Cuenta archivos leibles y no leibles
noLeibles = folder.archivosnoLeibles()
leibles = folder.getArchivosTexto()
conteo = 0



# si hay archivos leibles cuenta las palabras
if leibles > 0:
    conteo = folder.contarTotal()

#si la carpeta no tiene archivos de texto leibles muestra mensaje
if noLeibles > 0 and leibles == 0:
    print("LA CARPETA NO CONTIENE ARCHIVOS DE TEXTO QUE PUEDAN CONTENER LA PALABRA "+palabra)
#si la carpeta no tiene archivos de texto leibles o no leibles muestra mensaje
elif noLeibles == 0 and leibles == 0:
    print("LA CARPETA NO CONTIENE ARCHIVOS")
else:
    print("LA PALABRA " + palabra + " SE REPITE " + str(conteo) + " VECES EN LA CARPETA " + ruta)
    
    