
import json
#import direccion 
import client

class paresearFile():
    def __init__(self,file):
        self.file = file
        self.load() 
        if(self.data['tipo'] == 'GOLD'):
          self.cliente = client.Gold(self.data)
        elif(self.data['tipo'] == 'BLACK'):
          self.cliente = client.Black(self.data)
        else:
          self.cliente = client.Classic(self.data)

    def load(self):
      with open(self.file) as file:
        try:
          self.data = json.load(file)
        except FileNotFoundError as error: 
          print(error)



