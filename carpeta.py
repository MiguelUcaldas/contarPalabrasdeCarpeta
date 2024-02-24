import os
from archivo import archivo
class carpeta:

    # Contructor de la clase carpeta que recibira la ruta de la carpeta y un arreglo de archivos 
    # que se encuentran en la carpeta, los archivos se agregaran luego a la lista de archivos de la carpeta
    def __init__(self, ruta, palabra):
        self.ruta = ruta
        self.lstrutas = []
        self.palabra = palabra
        self.lstArchivos = []
        self.palabraTotal = 0
        self.archivosNoTexto = 0
        self.archivosTexto = 0

    # metodo que usa la direccion de la carpeta para buscar los archivos que se encuentran en ella
    # y crea una lista con la ruta de los archivos y lo guarda en archivos de la carpeta
    def buscarArchivos(self):
        print("BUSCANDO ARCHIVOS")
        for root, dirs, files in os.walk(self.ruta):
            for file in files:
                print("ARCHIVO "+os.path.join(root, file)+ " CARGADO")
                self.lstrutas.append(os.path.join(root, file))
      
    
    #Metodo que revisa si la carpeta tiene archivos que no sean de texto y cuentos archivos no texto hay
    def archivosnoLeibles(self):
        for rutaArchivo in self.lstrutas:
            if rutaArchivo.endswith(".txt") == False:
                self.archivosNoTexto += 1
      
  

    
    #metodo que crea un objeto de tipo archivo por cada ruta en la lista de rutas de la carpeta
    #y guarda el objeto en la lista de archivos de la carpeta y suma 1 a la variable archivosTexto
    def crearArchivos(self):
        print("CREANDO ARCHIVOS")
        for rutaArchivo in self.lstrutas:
            self.lstArchivos.append(archivo(rutaArchivo, self.ruta))
            self.archivosTexto += 1
        
    
    #metodo que recorre la lista de lstArchivos de la carpeta y cuenta las palabras que se repiten y retorna el total
    def contarTotal(self):
        for contenido in self.lstArchivos:
            self.palabraTotal += contenido.contarPalabras(self.palabra)
        return self.palabraTotal
       
    
 


    #setters y getters
    def getRuta(self):
        return self.ruta
    def setRuta(self, ruta):
        self.ruta = ruta
    def getLstrutas(self):
        return self.lstrutas
    def setLstrutas(self, lstrutas):
        self.lstrutas = lstrutas
    def getPalabra(self):
        return self.palabra
    def setPalabra(self, palabra):
        self.palabra = palabra
    def getLstArchivos(self):
        return self.lstArchivos
    def setLstArchivos(self, lstArchivos):
        self.lstArchivos = lstArchivos
    def getPalabraTotal(self):
        return self.palabraTotal
    def setPalabraTotal(self, palabraTotal):
        self.palabraTotal = palabraTotal
    def getArchivosNoTexto(self):
        return self.archivosNoTexto
    def setArchivosNoTexto(self, archivosNoTexto):
        self.archivosNoTexto = archivosNoTexto
    def getArchivosTexto(self):
        return self.archivosTexto
    def setArchivosTexto(self, archivosTexto):
        self.archivosTexto = archivosTexto


