from aad.aad import archivo_a_diccionario
from ac.ac import agregar_contacto
from mc.mc import modificar_contacto
from daa.daa import diccionario_a_archivo
from ec.ec import eliminar_contacto
from bc.bc import buscar_contacto
from ld.ld import listar_directorio
from me.me import menu 
def programa():
    while True:
        opcion=menu()
        if opcion == "0":
            print("Salir de la agenda...")
            exit()
        elif opcion=="1":
            print("Listando la agenda:")
            listar_directorio() #utilizo el modulo donde se encuentra la funcion listar directorio
        elif opcion=="2":
            agregar_contacto() #utilizo el modulo donde se encuentra la funcion agregar contacto
        elif opcion=="3":
            legajo=input("Ingrese el numero de legajo a buscar: ") #pido que ingrese el legajo
            buscar_contacto(legajo) #utilizo el modulo donde se encuentra la funcion buscar contacto
        elif opcion=="4":
            legajo=input("Ingrese el numero de legajo a eliminar: ") #pido que ingrese el numero de legajo a eliminar
            eliminar_contacto(legajo) #utilizo el modulo que contiene la funcion eliminar legajo
        elif opcion=="5":
            legajo=input("Ingrese el numero de legajo a modificar: ") #utilizo el modulo que contiene la funcion modificar contacto
            modificar_contacto(legajo)