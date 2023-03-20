from daa.daa import diccionario_a_archivo #importo los modulos a utilizar
from aad.aad import archivo_a_diccionario
def modificar_contacto(legajo):
    lista=[] #creo lista y diccionario
    directorio=archivo_a_diccionario()
    y=True #creo variable para preguntar en el ciclo si el usuario desea continuar modificando informacion 
    if legajo in directorio.keys(): #consulto si el legajo existe en el diccionario
        while y: 
            print(legajo,directorio[legajo]) #imprimo el diccionario
            lista=directorio[legajo] #creo una lista con la informacion de la key del legajo que deseo
            x=int(input("Menu de opcion a modificar: \n1- Nombre\n2- Número de celular \n3- DNI \n4- Dirección \n5- Grupo Sanguíneo \n6- Estado Civil \nElija su opción: "))
            #modifico el valor seleccionado y lo agrego a la lista creada
            if x==1:
                i=input("ingrese el Nombre modificado: ") 
                lista[0]=i
            elif x==2:
                i=input("ingrese el Celular modificado: ")
                lista[1]=i
            elif x==3:
                i=input("Ingrese el DNI modificado: ")
                lista[2]=i
            elif x==4:
                i=input("ingrese la Dirección modificada: ")
                lista[3]=i
            elif x==5:
                i=input("Ingrese el Grupo sanguíneo modificado: ")
                lista[4]=i
            elif x==6:
                i=input("ingrese el estado civil modificado: ")
                lista[5]=i
            directorio[legajo]=lista #agrego la informacion modificada en la lista creada y se la asigno a la key legajo del diccionario
            diccionario_a_archivo(directorio) #utilizo el modulo con la funcion diccionario a archivo y grabo el diccionario modificado
            x=input("Si desea continuar modificando ingrese 1, caso contrario ingrese cualquier caracter: ")
            if x=="1":
                y=True
            else:
                y=False
                
    else:
        print("El legajo no existe en la agenda")