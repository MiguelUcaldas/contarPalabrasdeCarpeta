#clase principal que se encarga de crear un objeto de tipo carpeta que se solicita la ruta por consola
# y luego se crea una lista con los archivos que se encuentran en la carpeta
# y se crea un objeto de tipo archivo por cada archivo en la lista
# y se leen los archivos y se cuentan las palabras que se repiten
# y se imprime el resultado
from carpeta import carpeta
import os

#solicita palabra a buscar
palabra = input("Ingrese la palabra a buscar: ")
#Recibe ruta
ruta = input("Ingrese la ruta de la carpeta donde buscara: ")

#Crea objeto carpeta
folder =  carpeta(ruta, palabra)
#Busca archivos en la carpeta
folder.buscarArchivos()
#Crea archivos
folder.crearArchivos()
#Cuenta las palabras
conteo = folder.contarTotal()
noLeibles = folder.getArchivosNoTexto()
leibles = 0+folder.getArchivosTexto()

print("Archivos no leibles: " + str(noLeibles))

if noLeibles > 0 and leibles == 0:
    print("La carpeta no contiene archivos de texto")
else:
    print("La palabra " + palabra + " se repite " + str(conteo) + " veces en la carpeta " + ruta)
    
    