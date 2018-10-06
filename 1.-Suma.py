# 	Resolver un programa que de como resultado de la siguiente suma
#	1+2+3+4+5+6+7+8+9
#	r=45
def suma(n): ##Se declara una funcion para controlar la recursividad del problema
	print(n)
	if n==1: ##Se condiciona el parametro que sea igual a 1 para que al llegar a este numero el programe pare
		return 1 ##Cuando la funcion llega a 1 retorna 1
	else:
		return suma (n-1) + n ##De lo contrario manda a llamarse a si misma con un digito menos y lo suma a n 
		
def main(): ##Funcion que sirve para imprimir el resultado y mandar el numero
	print(suma(9))
	
	
main() ##Se manda a llamar a la funcion main 