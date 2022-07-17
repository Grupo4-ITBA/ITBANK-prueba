class Direccion:

    def __init__(self, calle, numero, ciudad, provincia, pais):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.provincia = provincia
        self.pais = pais
        print("Direccion creada con exito!")
    
    def __str__ (self):
        return 'Calle: ' +self.calle + 'Numero: ' + str(self.numero) + ' Pais: ' + self.pais +' Provincia: ' + self.provincia + 'Ciudad: ' + self.ciudad