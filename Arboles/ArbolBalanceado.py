import os ## Libreria que me permite limpiar pantalla
class Nodo(object):
	
	def __init__(self, dato):
		self.dato = dato
		self.izquierda = None
		self.derecha = None
	
	def __str__(self):
		return '%s' % (self.dato) 
	
class Arbol(object):
	
	def __init__(self):
		self.root = None
	
	def agregar(self,dato):
		if self.root == None:
			print("\n\tDato ingresado")
			self.root = Nodo(dato)
		else:
			aux = self.root
			padre = None
			while aux != None:
				padre = aux
				if dato >= aux.dato:
					aux = aux.derecha
				else:
					aux = aux.izquierda
					
			if dato >= padre.dato:
				padre.derecha = Nodo(dato)
			else:
				padre.izquierda = Nodo(dato)
	
	def preorden(self,dato):
		if dato != None:
			print(dato)
			self.preorden(dato.izquierda)
			self.preorden(dato.derecha)
	
	def posTorden(self,dato):
		if dato != None:
			self.preorden(dato.izquierda)
			self.preorden(dato.derecha)
			print(dato)
			
	
	def inOrden(self,dato):
		if dato != None:
			self.preorden(dato.izquierda)
			print(dato)
			self.preorden(dato.derecha)
			

	def Raiz(self):
		return self.root
		
class Menu(object):
	
	def __init__(self):
		self.opc = None
	
	def Imprimir(self):
		up =  Arbol()
		
		while (True):
			print("\n\tArbol Binario")
			print("\n\t1.-Agregar\n\t2.-Preorden\n\t3.-Postorden\n\t4.-Inorden\n\t5.-Salir")
			self.opc = int(input("\n\tIngresa una opcion: "))
			os.system("clear") ## Limpia la pantalla
			
			if self.opc == 1:
				item = int(input("\n\tIngrese dato: "))
				up.agregar(item)
			elif self.opc == 2:
				print("\n\tPreorden")
				up.preorden(up.Raiz())
			elif self.opc == 3:
				print("\n\tPostorden")
				up.posTorden(up.Raiz())
			elif self.opc == 4:
				print("\n\tInorden")
				up.inOrden(up.Raiz())
			elif self.opc == 5:
				exit() ## Se sale del programa
			else:
				print("\n\tIngrese opcion correcta")
			 
		
op = Menu()

op.Imprimir()		