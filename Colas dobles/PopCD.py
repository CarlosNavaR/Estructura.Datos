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
			
	def PopRear(self): ## Funcion que nos permitira eliminar por el final
		if self.Front != self.Rear: ## Siempre y cuando sean diferentes los punteros no permitira eliminar
			self.Rear += 1 ## Como en la funcion de ingresar por este lado decrementa en este caso debe aumentar
			self.datos[self.Rear] = 0 ## Deja el valor como 0 
			aux = self.datos[self.Rear-1] ## Recorre el valor
		else:
			print("\n\tNo hay datos para eliminar")
	
	def PopFront(self):
		if self.Front != self.Rear: ## Siempre y cuando sean diferentes los punteros no permitira eliminar
			self.Front -= 1 ## Le quita un valor al frente
			self.datos[self.Front] = 0 ## Se elimina el valor asignandole 0 ya que lo tomo como null
			aux = self.datos[self.Front+1] ## Avanza el puntero
		else:
			print("\n\tNo hay datos para eliminar")
	def Menu(self): ## Funcion que nos mostrara las opciones que tenemos para realizar
		
		while True: ## Ciclo que siempre esta activo para poder ejecutar el menu las veces que deseen
			print("\n1.-pushRear \n2.-pushFront \n3.-PopRear \n4.-PopFront \n9.-Salir")
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
			elif opc == 3:
				self.PopRear() ## ELimina un dato del final
			elif opc == 4:
				self.PopFront() ## ELimina el dato por el fente
			elif opc==9: ## Se sale del menu
				exit() ## Sentencia que cierra el programa			
			else : ## SI ingresa una opcion diferente a las que se muestran en pantalla
				print("\nOpcion invalida") ## Se imprime un mensaje de error
			

up = Bicola()
up.Menu()	
		