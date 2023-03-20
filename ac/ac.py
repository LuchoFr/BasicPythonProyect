from aad.aad import archivo_a_diccionario
def agregar_contacto(): #creamos la linea del archivo 
    diccionario=archivo_a_diccionario() #pasamos el archivo a un diccionario con la funcion archivo_a_diccionario utilizada desde otro modulo
    print("-------------Agregar un contacto-------------")
    renglon = [] #creamos una lista vacia 
    numero_de_legajo = input("Ingrese el numero de legajo a agregar: ")
    if numero_de_legajo in diccionario.keys(): #hacemos un if en caso de que el legajo que ingrese ya exista y le informamos que ingrese a las otras opciones del menu para modificar o eliminarlo
        print("El numero de lejajo existe y pertenece a:",diccionario[numero_de_legajo][0],".")
        print("Si desea modificarlo o eliminarlo acceda desde el menu.")
    else: 
        #Solicito al Usuario ingresar todos los datos
        diccionario={}
        nombre_y_apellido = input("Ingrese el Nombre y Apellido: ")
        renglon.append(nombre_y_apellido + ",") #Agrego a la lista renglon los datos de la misma que van a ser los Values del diccionario
        telefono = input("Ingrese el Numero de Celular: ")
        renglon.append(telefono + ",")
        dni = input("Ingrese el N° de DNI: ")
        renglon.append(dni+ ",") 
        direccion = input("Ingrese la direccion del contacto: ")
        renglon.append(direccion+ ",") 
        grupo_sanguineo = input("Ingrese el grupo sanguineo: ")
        renglon.append(grupo_sanguineo+ ",") 
        estado_civil = input ("Ingres el estado civil de la persona a agregar: ")
        renglon.append(estado_civil)
        #Agrego la key que va a ser el numero de legajo y le asigno la lista renglon
        diccionario [numero_de_legajo]=renglon
        #Abro el archivo en forma Append
        nombre_de_archivo="agenda.txt"
        archivo=open(nombre_de_archivo,"a")
        #Itero sobre el diccionario para grabar en el archivo los valores
        for legajo,informacion in diccionario.items():
            #Grabo el valor de la key en el archivo
            archivo.write(legajo+",")
            #Itero sobre la lista de informacion
            for x in range (0,6):
            #Guardo la informacion de la lista en el archivo(En este caso 0-6 por la cantidad de elementos de la lista)
                archivo.write(informacion[x])
            archivo.write("\n")
        archivo.close()  