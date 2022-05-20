class Flor:
    __numeroActual=0
    __numero=0
    __nombre=''
    __color=''
    __descripcion=''
    __maximaCantidadPedida=0
    @classmethod
    def getNumero(cls):
        cls.__numeroActual+=1
        return cls.__numeroActual
    def __init__(self,nombre='',color='',descripcion=''):
        self.__numero=self.getNumero()
        self.__nombre=nombre
        self.__color=color
        self.__descripcion=descripcion
        self.__maximaCantidadPedida=0
    def mostrarFlor(self):
        print('{}) Nombre:{}, Color:{}'.format(self.__numero,self.__nombre,self.__color))
    def obtenerNumero(self):
        return self.__numero
    def verificarNumero(self,numero):
        resultado=False
        if self.__numero==numero:
            resultado=True
        return resultado
    def setMaximaCantidad(self,cantidad):
        self.__maximaCantidadPedida=cantidad
    def getMaximaCantidad(self):
        return self.__maximaCantidadPedida
    def __str__(self):
        return self.__nombre
    def __gt__(self,otraFlor):
        resultado=False
        if type(otraFlor)==Flor:
            resultado=self.__maximaCantidadPedida>otraFlor.getMaximaCantidad()
        return resultado