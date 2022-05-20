import csv,numpy as np
from Flor import Flor
class ManejadorFlor:
    __arregloFlores=None
    __cantidad=0
    __dimension=0
    __incremento=0
    def __init__(self,dimension=3,incremento=5):
        self.__arregloFlores=np.empty(dimension,dtype=Flor)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def agregarFlor(self,flor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionarArreglo()
        self.__arregloFlores[self.__cantidad]=flor
        self.__cantidad+=1
    def redimensionarArreglo(self):
        self.__arregloFlores.resize(self.__dimension)
    def cargarDesdeArchivo(self):
        nombreArchivo='flores.csv'
        archivo=open(nombreArchivo,encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarFlor(Flor(fila[0],fila[1],fila[2]))
        print('Fin de la carga desde: ',nombreArchivo)
    def cantidadFlores(self):
        return self.__cantidad
    def mostrarFlores(self):
        for i in range(self.__cantidad):
            self.__arregloFlores[i].mostrarFlor()
    def mostrarFlor(self,numero):
        iFlor=self.buscarFlor(numero)
        if iFlor!=-1:
            print(self.__arregloFlores[iFlor])
        else:
            print('Numero de flor incorrecto.')
    def buscarFlor(self,numero):
        resultado=-1
        bandera=True
        i=0
        while i<self.__cantidad and bandera:
            if self.__arregloFlores[i].verificarNumero(numero):
                bandera=False
                resultado=i
            i+=1
        return resultado
    def getFlor(self,numero):
        resultado=-1
        iFlor=self.buscarFlor(numero)
        if iFlor!=-1:
            resultado=self.__arregloFlores[iFlor]
        return resultado
    def verificarDimension(self):
        if self.__dimension!=self.__cantidad:
            self.__dimension=self.__cantidad
            self.redimensionarArreglo()
    def ordenarPorNumero(self):
        for i in range(self.__cantidad-1):
            min=i
            for j in range(i+1,self.__cantidad):
                if self.__arregloFlores[j].obtenerNumero()<self.__arregloFlores[min].obtenerNumero():
                    min=j
            aux=self.__arregloFlores[i]
            self.__arregloFlores[i]=self.__arregloFlores[min]
            self.__arregloFlores[min]=aux
    def floresMasPedidas(self,manejadorRamo):
        print('5 flores mas pedidas:')
        self.verificarDimension()
        cantidadBusqueda=0
        if self.__cantidad>5:
            cantidadBusqueda=5
        else:
            cantidadBusqueda=self.__cantidad
        for i in range(self.__cantidad):
            numero=self.__arregloFlores[i].obtenerNumero()
            self.__arregloFlores[i].setMaximaCantidad(manejadorRamo.mayorCantidadVendida(numero))
        self.__arregloFlores[::-1].sort()
        bandera=True
        i=0
        while i<cantidadBusqueda and bandera:
            if self.__arregloFlores[i].getMaximaCantidad()==0:
                bandera=False
            else:
                print(self.__arregloFlores[i])
                i+=1
        self.ordenarPorNumero()