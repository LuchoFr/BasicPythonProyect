from aad.aad import archivo_a_diccionario #importamos el modulo a utilizar 
def listar_directorio(): #mostramos el directorio completo
    directorio=archivo_a_diccionario() #paso la informacion que se encuentra en el archivo agenda.txt a un diccionario y luego la listo
    print(directorio)
