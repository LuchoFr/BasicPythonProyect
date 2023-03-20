def archivo_a_diccionario(): #leemos la agenda del archivo al diccionario
    agenda={}
    lista_de_informacion_de_agenda=[] #creamos la lista que va a ser el value asignado a la key de numero de contacto del diccionario
    nombre_de_archivo="agenda.txt"
    archivo=open(nombre_de_archivo,"r")
    lista_de_contactos=archivo.readlines() #leo todo el directorio con una lista
                                           #un elemento en la lista por cada renglon del txt 

    for elemento in lista_de_contactos:
        campos=elemento.strip().split(",") #la informacion quedara separada por el caracter ","
        lista_de_informacion_de_agenda=[]
        for i in range(0,6):
            lista_de_informacion_de_agenda.append(campos[i+1])#creo una lista con los valores de informacion del contacto para asignar a la key de numero de contacto
        agenda[campos[0]]=lista_de_informacion_de_agenda#estoy asignando el primer valor a la key (numero de contacto) y a cada key una lista con su informacion  
    archivo.close()
    return agenda