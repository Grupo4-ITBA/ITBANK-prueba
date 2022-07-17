from fileinput import close
from pydoc import cli
from Classes.Cliente import *
from Classes.Reader import Reader
from Classes.Direccion import Direccion
import sys

data = Reader(sys.argv[1])
direcciones = data.file["direccion"]
reason = " "
dataheaderCliente = "Nombre,Apellido,DNI,Numero,Tipo"
dataheaderDirec = "Pais,Provincia,Ciudad,Calle,Numero"
dataheaderCTrans = "Fecha,Tipo,Estado,Monto,Detalles"

#Verifico tipo de cliente

if data.file["tipo"] == "CLASSIC":
    cliente = Classic(data.file["numero"],data.file["nombre"],data.file["apellido"],data.file["dni"])
    

if data.file["tipo"] == "GOLD":
    cliente = Gold(data.file["numero"],data.file["nombre"],data.file["apellido"],data.file["dni"])

if data.file["tipo"] == "BLACK":
    cliente = Black(data.file["numero"],data.file["nombre"],data.file["apellido"],data.file["dni"])

#Creo direccion del Cliente
direccion = Direccion(direcciones["calle"],direcciones["numero"],direcciones["ciudad"],direcciones["provincia"],direcciones["pais"])


#Empiezo a formatear la tabla

#Row de Cliente y Direccion

rowCliente = data.file["nombre"] + ',' + data.file["apellido"] + ',' + data.file["dni"] + ',' + str(data.file["numero"]) + ',' + data.file["tipo"]
rowDireccion = direcciones["pais"] + ',' + direcciones["provincia"] + ',' + direcciones["ciudad"]+ ',' + direcciones["calle"]+ ',' + direcciones["numero"]
rowTrans = []

fileout = open("reporte.html", "w")

table = "<table>\n"

# Create the table's column headers
header = dataheaderCliente.split(",")
table += "  <tr>\n"
for column in header:
    table += "    <th>{0}</th>\n".format(column.strip())
table += "  </tr>\n"

# Create the table's row data
row = rowCliente.split(",")
table += "  <tr>\n"
for column in row:
    table += "    <td>{0}</td>\n".format(column.strip())
table += "  </tr>\n"

# Create the table's column headers
header = dataheaderDirec.split(",")
table += "  <tr>\n"
for column in header:
    table += "    <th>{0}</th>\n".format(column.strip())
table += "  </tr>\n"

# Create the table's row data
row = rowDireccion.split(",")
table += "  <tr>\n"
for column in row:
    table += "    <td>{0}</td>\n".format(column.strip())
table += "  </tr>\n"

# Create the table's column headers
header = dataheaderCTrans.split(",")
table += "  <tr>\n"
for column in header:
    table += "    <th>{0}</th>\n".format(column.strip())
table += "  </tr>\n"



for x in data.file["transacciones"]:
    if x["estado"] == "RECHAZADA":
        if x["tipo"] == 'TRANSFERENCIA_RECIBIDA': reason = cliente.transferencia_recibida(x["monto"])
        if x["tipo"] == 'COMPRA_DOLAR': reason = cliente.puede_comprar_dolar(x["monto"],x["cupoDiarioRestante"])
        if x["tipo"] == 'ALTA_CHEQUERA': reason = cliente.puede_crear_chequera(x["totalChequerasActualmente"])
        if x["tipo"] == 'ALTA_TARJETA_CREDITO': reason = cliente.puede_crear_tarjeta_credito(x["totalTarjetasDeCreditoActualmente"])
        if x["tipo"] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO': reason = cliente.puede_retirar_dinero(x["monto"],x["cupoDiarioRestante"],x["saldoEnCuenta"])
        if x["tipo"] == 'TRANSFERENCIA_ENVIADA': reason = cliente.transferencia_enviada(x["monto"],x["cupoDiarioRestante"])
    try:  
        rowTrans.append(x["fecha"] + ',' + x["tipo"] + ',' + x["estado"] + ',' + str(x["monto"]) + ',' + reason) 
    except:
        print("Formato de transaccion incorrecto. ")
    reason = " "   

# Create the table's row data
for line in rowTrans:
    row = line.split(",")
    table += "  <tr>\n"
    for column in row:
        table += "    <td>{0}</td>\n".format(column.strip())
    table += "  </tr>\n"



table += "</table>"

fileout.writelines(table)
fileout.close()

print("reporte.html generado con exito!")


# tipos tran = "TRANSFERENCIA_RECIBIDA", "COMPRA_DOLAR", "ALTA_CHEQUERA", "ALTA_TARJETA_CREDITO", 
# "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "TRANSFERENCIA_ENVIADA"