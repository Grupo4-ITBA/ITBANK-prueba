from asyncio.windows_events import NULL
import csv
from dataclasses import Field
from datetime import *

archivo = input("Ingrese la ruta del archivo que quiere leer.. ")
listAll = input("Quire listar todos los cheques? (Y/N)...")
if listAll == 'N':
    dni = input("Ingrese su DNI... ")
    tipoC = input("EMITIDO o DEPOSITADO?.. ")
    estadoC = input("Estado del cheque? (PENDIENTE/APROBADO/RECHAZADO).. ")
    # d1, m1, y1 = [int(x) for x in input("Fecha desde (ex. 01-April-2021).. ").split('-')]
    # d2, m2, y2 = [int(x) for x in input("Fecha hasta (ex. 01-April-2021).. ").split('-')]
    dateFro = input("Fecha desde (ex. 01-April-2021).. ")
    dateTo = input("Fecha hasta (ex. 01-April-2021).. ")
    # dateT = input("Fecha desde (ex. 01-April-2021).. ")
    # if d1 != '' and d2 != '':
    #     dateFro = date(y1, m1, d1)
    #     dateTo = date(y2, m2, d2)

with open(archivo, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    reader_line = 0
    if reader_line == 0:
            fields = ''
            for field in csv_reader.fieldnames:
                fields += field + ' '
            print(fields)
            reader_line += 1
    for row in csv_reader:
        correctedDateOg = datetime.fromtimestamp(int(row['FechaOrigen'])).strftime("%d-%B-%Y")
        correctedDatePa = datetime.fromtimestamp(int(row['FechaPago'])).strftime("%d-%B-%Y")
        if listAll == 'Y':
            print(row['NroCheque'] + ' ' + row['CodigoBanco'] + ' ' + row['CodigoScurusal'] + ' ' + row['NumeroCuentaOrigen'] + ' ' + row['NumeroCuentaDestino'] + ' ' + row['Valor'] + ' ' + correctedDateOg + ' ' + correctedDatePa + ' ' + row['DNI'] + ' ' + row['Tipo'] + ' ' + row['Estado'])
        elif estadoC == '' and dateFro == '' and dateTo == '':
            if dni == row['DNI'] and tipoC == row['Tipo']:
                print(row['NroCheque'] + ' ' + row['CodigoBanco'] + ' ' + row['CodigoScurusal'] + ' ' + row['NumeroCuentaOrigen'] + ' ' + row['NumeroCuentaDestino'] + ' ' + row['Valor'] + ' ' + correctedDateOg + ' ' + correctedDatePa + ' ' + row['DNI'] + ' ' + row['Tipo'] + ' ' + row['Estado'])
        elif estadoC == '':
            if dni == row['DNI'] and tipoC == row['Tipo'] and dateFro <= correctedDateOg >= dateTo and dateFro <= correctedDatePa >= dateFro:
                print(row['NroCheque'] + ' ' + row['CodigoBanco'] + ' ' + row['CodigoScurusal'] + ' ' + row['NumeroCuentaOrigen'] + ' ' + row['NumeroCuentaDestino'] + ' ' + row['Valor'] + ' ' + correctedDateOg + ' ' + correctedDatePa + ' ' + row['DNI'] + ' ' + row['Tipo'] + ' ' + row['Estado'])
        elif dateFro == '' and dateTo == '':
            if dni == row['DNI'] and tipoC == row['Tipo'] and estadoC == row['Estado']:
                print(row['NroCheque'] + ' ' + row['CodigoBanco'] + ' ' + row['CodigoScurusal'] + ' ' + row['NumeroCuentaOrigen'] + ' ' + row['NumeroCuentaDestino'] + ' ' + row['Valor'] + ' ' + correctedDateOg + ' ' + correctedDatePa + ' ' + row['DNI'] + ' ' + row['Tipo'] + ' ' + row['Estado'])
        else:
            print("Falta algun dato!")

        
        
