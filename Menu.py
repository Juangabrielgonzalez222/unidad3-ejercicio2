from Ramo import Ramo

class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.salir
        }
    def lanzarMenu(self,manejadorFlor,manejadorRamo):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para  registrar un ramo vendido.')
            print('-Ingrese 2 para mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.')
            print('-Ingrese 3 para ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.')
            print('-Ingrese 4 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<4:
                ejecutar(manejadorFlor,manejadorRamo)
            else:
                ejecutar()
    def opcion1(self,manejadorFlor,manejadorRamo):
        print('Tamaños:')
        print('1: chico, 2: mediano, 3: grande')
        tamaño=self.cargarNumeroEntero('Ingrese numero del tamaño de ramo:')
        if tamaño>0 and tamaño<4:
            if tamaño==1:
                tamaño='chico'
            elif tamaño==2:
                tamaño='mediano'
            else:
                tamaño='grande'
            ramo=Ramo(tamaño)
            bandera=True
            print('A continuacion se deben cargar las flores del ramo, para finalizar la carga ingrese s')
            while bandera:
                manejadorFlor.mostrarFlores()
                valorIngresado=input('Ingrese numero de flor o s:')
                if valorIngresado=='s':
                    bandera=False
                else:
                    try:
                        valorIngresado=int(valorIngresado)
                    except ValueError:
                        print('ERROR: Se debe ingresar un numero entero o para finalizar la carga ingrese s.')
                    else:
                        flor=manejadorFlor.getFlor(valorIngresado)
                        if flor!=-1:
                            ramo.agregarFlor(flor)
                        else:
                            print('Numero de flor incorrecto.')
            manejadorRamo.agregarRamo(ramo)
        else:
            print('Tamaño de ramo incorrecto.')
    def opcion2(self,manejadorFlor,manejadorRamo):
        manejadorFlor.floresMasPedidas(manejadorRamo)
    def opcion3(self,manejadorFlor,manejadorRamo):
        print('Tamaños:')
        print('1: chico, 2: mediano, 3: grande')
        tamaño=self.cargarNumeroEntero('Ingrese numero del tamaño de ramo:')
        if tamaño==1:
            tamaño='chico'
        elif tamaño==2:
            tamaño='mediano'
        elif tamaño==3:
            tamaño='grande'
        else:
            tamaño=-1
        if tamaño!=-1:
            manejadorRamo.mostrarFloresVendidas(tamaño,manejadorFlor)
        else:
            print('El valor ingresado no corresponde.')
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')