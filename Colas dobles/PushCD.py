import os ## Libreria que permite usar la sentencia os.system("clear")

class Bicola(object): ## Se crea una clase que contendra las funciones con las respectivas operaciones
	def __init__(self):#0 1 2 3 4 5 6 7 8 9
		self.datos =   [0,0,0,0,0,0,0,0,0,0] ## se crea e inicializa el arreglo en 0
		self.Front = 0 # Se declaran e inicializan los apuntadores
		self.Rear = 0 #

		
	def pushFront(self,item):  ## Funcion que nos permitira ingresar los valores por el frente de la cola
		if self.Front == 5: ## Se condiciona a que cuando el front llegue a 5 sea el maximo esto para igualar ambos lados a 5 y tengan la misma capacidad
			print("\n\ttLimite de 5 elementos por lado")
		else:
			self.Front += 1 ## Se incrementa el valor del puntero front
			self.datos[self.Front] = item ## Se ingresan los datos al arreglo/lista
			print("\n\tDato insertado correctamente")
	
	def pushRear(self,item): ## Funcion que permite ingresar por el final de la cola
		if self.Rear == -5:  ## Funcion que nos permitira ingresar los valores por el frente de la cola
			print("\n\tLimite de 5 elementos por lado")
		else:
			self.Rear -= 1 ## Se decrementa el valor del puntero
			self.datos[self.Rear] = item ## Se ingresan los datos al arreglo/lista
			print("\n\tDato insertado correctamente")
	def Menu(self): ## Funcion que nos mostrara las opciones que tenemos para realizar
		
		while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen
			print("\n1.-pushRear \n2.-pushFront \n9.-Salir")
			opc = int(input("\n\tIngresa opcion\t-> "))
			os.system("clear")## Limpia la pantalla
			
			if opc == 1:
				x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
				print("")
				self.pushRear(x) ## Ingresa datos por el final
			elif opc == 2:
				x=int(input("\n\tIngresa dato para almacenar -> ")) ## Pide el dato que sera enviado a la funcion push
				print("")
				self.pushFront(x) ## Ingresa datos por el frente
			elif opc==9: ## Se sale del menu
				exit() ## Sentencia que cierra el programa			
			else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
				print("\nOpcion invalida") ## Se imprime un mensaje de error
			

up = Bicola()
up.Menu()	