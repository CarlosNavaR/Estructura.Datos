## Hacer un programa que simule la fila de clientes de una tienda de super mercado,
## Considerando que solo hay una caja activa. La fila solo puede tener como maximo
## 5 Clientes 
import os
index = 0
class Tienda(): ## Clase que almacena las operaciones de la cola

	def __init__(self): ##Inicializa la lista
		self.fila = [0,0,0,0,0]
	
	def push(self,dato): ##Ingresa los datos a la cola
		global index
		self.fila[index] = dato
		index+=1
	
	def peek(self): ##Elimina un elemento de la lista
		global index
		if index!=0:
			print(str("\n\tCliente con el numero: [" + str(self.fila[0])) + "] Procedio a pagar y dejo un lugar libre")
			for i in range(0,4):
				self.fila[i] = self.fila[i+1]
			self.fila[4]=0
			index -=1
		else:	
			print("\n\tFila libre; Puede ingresar")

def menuTienda(): ## Bloque que maneja los datos de la fila 
	fila = Tienda()
	while True:
		print("\n\tBienvenidos abarrotes 'chochito'\n")
		print("\t\tQue desea:")
		print("\t1.-Unirse a la fila\n\t2.-Atender cliente\n\t3.-Cerrar caja\n")
		dato = int(input("\tIngrese su opcion -> "))
		os.system("clear")
		if dato==1:
			if index <= 4:
				numero = int(input("\n\tIngresa numero de cliente -> "))
				fila.push(numero)
			else:
				print("\n\t3Espere que alguien sea atendido para poder ingresar")
		elif dato==2:
			fila.peek()

			
		elif dato==3:
			exit()
		else:
			print("\n\t\tOpcion invalida")
	
menuTienda()
	
		
	
	
		