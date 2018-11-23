import os

class  Nodo():
	
	def __init__(self, dato):
		self.dato = dato
		self.izquierda = None
		self.derecha = None
	
	def __str__(self):  ## Se redefine el metodo para que nos muestre los datos
		return '%s' % (self.dato)  ## Nos retorna el valor en forma de string para poder ser mostrado
		
class OpBinario():
	
	def __init__(self):
		self.root = None
	
	def Ingresar(self,item):
		
		
		