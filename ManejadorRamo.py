from Ramo import Ramo

class ManejadorRamo:
    __listaRamos=[]
    def __init__(self):
        self.__listaRamos=[]
    def agregarRamo(self,ramo):
        if type(ramo)==Ramo:
            self.__listaRamos.append(ramo)
        else:
            print('Error, no se pudo agregar un ramo a la lista, el tipo de datos es incorrecto.')
    def mostrarFloresVendidas(self,tamaño,manejadorFlor):
        if len(self.__listaRamos)>0:
            print('Flores vendidas ramo',tamaño+':')
            cantidadFlores=manejadorFlor.cantidadFlores()
            for i in range(cantidadFlores):
                bandera=True
                j=0
                cantidadRamos=len(self.__listaRamos)
                while j<cantidadRamos and bandera:
                    if self.__listaRamos[j].verificarTamaño(tamaño):
                        if self.__listaRamos[j].verificarFlor(i+1):
                            bandera=False
                    j+=1
                if not bandera:
                    manejadorFlor.mostrarFlor(i+1)
                i+=1
        else:
            print('No hay ramos vendidos')
    def mayorCantidadVendida(self,numero):
        mayorCantidad=0
        for ramo in self.__listaRamos:
            cantidadFlores=ramo.cantidadFlores(numero)
            if cantidadFlores>mayorCantidad:
                mayorCantidad=cantidadFlores
        return mayorCantidad