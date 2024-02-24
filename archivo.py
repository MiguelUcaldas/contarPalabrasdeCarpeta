import carpeta
class archivo:
    # Contructor de la clase archivo que recibira la ruta del archivo y su contenido ademas 
    # tendra una variable para contar las veces que se repite una palabra en el archivo y 
    # guardara el id de la carpeta a la que pertenece el archivo
    def __init__(self, ruta ,carpeta):
        self.ruta = ruta
        self.carpeta = carpeta

    # Metodo que lee el archivo y cuenta las veces que se repite una palabra y retorna el total

    
    def contarPalabras(self, palabra):
        #convertir la palabra a minúsculas para la comparación
        palabra = palabra.lower()
        conteo = 0
        with open(self.ruta, 'r') as file:
            for line in file:
                line = line.lower()  # Convertir la línea a minúsculas
                line = ''.join(c for c in line if c.isalnum() or c.isspace())  # Eliminar caracteres no alfanuméricos excepto espacios
                words = line.split()
                for word in words:
                    if word == palabra.lower():  # Convertir la palabra a minúsculas para la comparación
                        conteo += 1
        print("La palabra "+palabra+" se repite "+str(conteo)+" veces en el archivo "+self.ruta)
        return conteo


    
        #setters y getters
    def getRuta(self):
        return self.ruta
    def setRuta(self, ruta):
        self.ruta = ruta
    def getContenido(self):
        return self.contenido
    def setContenido(self, contenido):
        self.contenido = contenido
    def getCarpeta(self):
        return self.carpeta