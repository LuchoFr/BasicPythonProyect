def diccionario_a_archivo(dir):
    nombre_de_archivo="agenda.txt"
    archivo=open(nombre_de_archivo,"w")
    for legajo,informacion in dir.items():
        #Grabo el valor de la key en el archivo
        archivo.write(legajo+",")
        #Itero sobre la lista de informacion
        for x in range (0,6):
        #Guardo la informacion de la lista en el archivo(En este caso 0-6 por la cantidad de elementos de la lista
            if x!=5: #utilizamos este if para no agregar una coma en el ultimo campo 
                archivo.write(informacion[x]+",")
            else:
                archivo.write(informacion[x])    
        archivo.write("\n")
    archivo.close()