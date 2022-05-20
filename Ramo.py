from Flor import Flor
class Ramo:
    __tamaño=''
    __listaFlores=[]
    def __init__(self,tamaño=''):
        self.__tamaño=tamaño
        self.__listaFlores=[]
    def agregarFlor(self,flor):
        if type(flor)==Flor:
            self.__listaFlores.append(flor)
        else:
            print('Error, no se pudo agregar una flor a la lista, el tipo de datos es incorrecto.')
    def verificarTamaño(self,tamaño):
        resultado=False
        if self.__tamaño==tamaño:
            resultado=True
        return resultado
    def verificarFlor(self,numero):
        resultado=False
        cantidadFlores=len(self.__listaFlores)
        i=0
        bandera=True
        while i< cantidadFlores and bandera:
            if self.__listaFlores[i].verificarNumero(numero):
                bandera=False
                resultado=True
            else:
                i+=1
        return resultado
    def cantidadFlores(self,numero):
        cantidad=0
        for flor in self.__listaFlores:
            if flor.verificarNumero(numero):
                cantidad+=1
        return cantidad