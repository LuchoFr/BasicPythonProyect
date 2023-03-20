from aad.aad import archivo_a_diccionario #importo los modulos a utilizar 
def buscar_contacto(legajo):
    directorio=archivo_a_diccionario() #creo un diccionario con la informacion en el archivo agenda.txt utilizando la funcion archivo a diccionario
    if legajo in directorio.keys(): #consulto si la key legajo esta en el diccionario
        lista=directorio[legajo] #creo una lista con la informacion de la key legajo de interes
        x=int(input("Ingrese el dato a consultar: \n1- Nombre\n2- Número de celular \n3- DNI \n4- Dirección \n5- Grupo Sanguíneo \n6- Estado Civil \nElija su opción: "))
        #muestro la informacion que el usuario solicita
        if x==1:
            print("------------------")
            print("NOMBRE:" ,lista[0])
        elif x==2:
            print("------------------")
            print("N° CELULAR: ",lista[1])
        elif x==3:
            print("------------------")
            print("DNI: ", lista[2])
        elif x==4:
            print("------------------")
            print("DIRECCIÓN: ",lista[3])
        elif x==5:
            print("------------------")
            print("GRUPO SANGUÍNEO: ",lista[4])
        elif x==6:
            print("------------------")
            print("ESTADO CÍVIL: ",lista[5])
    else:
        print("no existe el legajo")