from ManejadorFlor import ManejadorFlor
from ManejadorRamo import ManejadorRamo
from Menu import Menu

if __name__== '__main__':
	cantidad=None
	bandera=True
	while bandera:
		try:
			cantidad=int(input('Ingrese cantidad de flores:\n'))
		except ValueError:
			print('Ingrese un numero entero.')
		else:
			bandera=False
	manejadorFlor=ManejadorFlor(cantidad,5)
	manejadorFlor.cargarDesdeArchivo()
	manejadorRamo=ManejadorRamo()
	menu=Menu()
	menu.lanzarMenu(manejadorFlor,manejadorRamo)