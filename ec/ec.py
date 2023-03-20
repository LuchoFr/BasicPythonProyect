from daa.daa import diccionario_a_archivo #importo los modulos a utilizar
from aad.aad import archivo_a_diccionario
def eliminar_contacto(legajo):
    directorio=archivo_a_diccionario() #pasamos el archivo a un diccionario con la funcion archivo_a_diccionario utilizada desde otro modulo
    if legajo in directorio.keys(): #consultamos si la key legajo se encuentra en el diccionario
        print("El numero de legajo "+legajo+" perteneciente a "+directorio[legajo][0]+" fue eliminado")
        del directorio[legajo] #eliminamos la key legajo y su informacion del diccionario
        diccionario_a_archivo(directorio) #utilizamos la funcion importada del modulo para guardar el diccionario al archivo
    else:
        print("El Legajo no se encuentra en la agenda")