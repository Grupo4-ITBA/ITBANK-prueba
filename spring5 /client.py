class Cuenta: 
    def __init__(self):
        pass
    def limite_extraccion_diario(self):
        pass
    def limite_tranferencia_recibida(self):
        pass
    def monoto(self):
        pass
    def costo_tranferencia(self):
        pass
    def saldo_decubierto_disponible(self):
        pass

class Client:
    def __int__(self, data):
       self.name = data
       self.apellido = data
       self.dni = data 
       self.tipo = data
       print('Se creo el cliente con DNI'+ self.dni)

    def puede_crear_chequera():
        pass
    def puede_crear_tarjeta_credito():
        pass 
    def puede_comprar_dolar():
         pass

class Classic(Client,Cuenta):
     def __init__(self, data):
       print('Categoría: Classic')
       super().__init__(data)
       self.tarjeta_debito = True

     def limite_extraccion_diario(self):
        self.limite = 10000

     def puede_crear_tarjeta_credito(self):
         return False

     def puede_crear_chequera():
        return False


class Gold(Client):
    def __init__(self, data):
        print('Categoría: Gold')
        super().__init__()
       
    
class Black(Client):
    def __init__(self, data):
        print('Categoría: Black')
        super().__init__(data)
        
    
