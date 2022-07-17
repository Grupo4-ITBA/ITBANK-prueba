class Cliente:

    def __init__(self,numero, nombre, apellido,  dni):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        print("Cliente creado con exito!")
    
    def __str__ (self):
        return 'Numero: ' + str(self.numero) + ' Nombre: ' +self.nombre+ ' ' + self.apellido + ' DNI: ' + str(self.dni) 

class Classic(Cliente):

    def puede_retirar_dinero(self,monto,maximo, saldo):
        if monto > maximo:
            return "Excedio el limite diario. "
        if monto > saldo:
            return "Saldo en cuenta insuficiente. "

    def puede_crear_chequera(self, chequeras):
        return "Clientes classic no pueden tener chequeras. "
    
    def puede_crear_tarjeta_credito(self, tarjetas):
        return "Clientes classic no pueden sacar tarjetas de credito. "
    
    def puede_comprar_dolar(self,monto,maximo):
        return "Clientes classic no pueden comprar dolares. "
    
    def transferencia_recibida(self, monto):
        if monto > 150000: 
            return "Limite de tranferencia excedido"
    
    def transferencia_enviada(self, monto, maximo):
        maximo_real = maximo * 1.1
        if monto > maximo_real:
            return "Saldo insuficiente. "

class Gold(Cliente):

    def puede_retirar_dinero(self,monto,maximo, saldo):
        limite = saldo - monto
        if monto > maximo:
            return "Excedio el limite diario. "
        if limite < -10000 :
            return "Saldo en cuenta insuficiente. "

    def puede_crear_chequera(self, chequeras):
        if chequeras >= 1:
         return "El cliente ya cuenta con una chequera. "
    
    def puede_crear_tarjeta_credito(self, tarjetas):
        if tarjetas >= 1:
            return "El cliente ya cuenta con 1 tarjeta. "
    
    def puede_comprar_dolar(self,monto,maximo):
        if monto > maximo:
            return "Excedio el limite diario. "
    
    def transferencia_recibida(self, monto):
        if monto > 500000: 
            return "Limite de tranferencia excedido"
    
    def transferencia_enviada(self, monto, maximo):
        maximo_real = maximo * 1.05
        if monto > maximo_real:
            return "Saldo insuficiente. "

class Black(Cliente):

    def puede_retirar_dinero(self,monto,maximo, saldo):
        limite = saldo - monto
        if monto > maximo:
            return "Excedio el limite diario. "
        if limite < -10000 :
            return "Saldo en cuenta insuficiente. "

    def puede_crear_chequera(self, chequeras):
        if chequeras >= 2:
         return "El cliente ya cuenta con 2 chequeras. "
    
    def puede_crear_tarjeta_credito(self, tarjetas):
        if tarjetas >= 5:
            return "El cliente ya cuenta con 5 tarjetas. "
    
    def puede_comprar_dolar(self,monto,maximo):
        if monto > maximo:
            return "Excedio el limite diario. "
    
    def transferencia_recibida(self):
        return 
    
    def transferencia_enviada(self, monto, maximo):
        if monto > maximo:
            return "Saldo insuficiente. "