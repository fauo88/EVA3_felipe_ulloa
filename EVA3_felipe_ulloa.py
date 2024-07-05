import os
import time
import random
import csv
import json


def CargarDatos():
  with open('tiendas.json', 'r', encoding='utf-8') as archivo_tiendas:
   tiendas = json.load(archivo_tiendas)

  with open('vendedores.json', 'r', encoding='utf-8') as archivo_vendedores:
   vendedores = json.load(archivo_vendedores)
  
  with open('ventas.json', 'r', encoding='utf-8') as archivo_ventas:
   ventas = json.load(archivo_ventas)

  return tiendas, vendedores, ventas


def menu():
    print("---MENU---")
    print("1. Precargar ventas")
    print("2. Crear venta")
    print("3. Reporte de Sueldo")
    print("4. Ver estadisticas")
    print("5. Salir")

def error():
   print("Ingrese una de las opciones disponibles")  


def main(): 
   tiendas, vendedores, ventas=CargarDatos()
   while True:       
       opc1=0
       menu()
       try:
           opc1=int(input('Ingrese una opción: '))
       except:
           error()
       if opc1 < 0 or opc1 > 5:
           error()
       else:
           if opc1 == 1:
               print('Precargar ventas')
               CargarDatos()
               for venta in ventas:
                 idventa=venta['id_venta'{0}]
           
               
           elif opc1 == 2:
               print('Crear venta')
               
           elif opc1 == 3:
               print('Reporte de sueldos')
               
           elif opc1 == 4:
               print('Ver Estadísticas')
               
           elif opc1 == 5:
               os.system('cls')
               print('Cerrando la app!!!!')
               time.sleep(2)
               break

if __name__ == '__main__':
   main()