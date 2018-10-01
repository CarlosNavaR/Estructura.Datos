#include <iostream>
#define max 5 //Variable global inicializada en 5
using namespace std;

typedef struct //Estructura que controlara el arreglo 
{
	int items[max]= {0,0,0,0,0}; //Arreglo inicializado en 0 donde se almacenaran los datos
	int index=0; //Variable que controlara los datos
}pila; 


//Estado de la pila
int EvitarOver(pila Pila) //Funcion que controla que el arreglo no sobre pase su capacidad
{
	if(Pila.index == max-1)
		return 1;
	return 0;
}

int EvitarUnder(pila Pila) //Funcion que controla que el arreglo no reduzca su capacidad mas de lo que debe
{
	if (Pila.index==-1)
		return 1;
	return 0;
}

//Operaciones de las pilas
 
int push(pila *Pila, int dato) //Funcion de tipo entero que ingresa los datos al arreglo controlado por un punteroo
{
	if(EvitarOver(*Pila)==0) //Se condiciona que el arreglo tenga espacios para poder ingresar datos
	{ 
	 	Pila->index++; //Se incrementa la variable que trabaja con la cantidad de datos
		Pila->items[Pila->index]=dato;  //Se agregan los datos a la pila; Se accede a la pila con apuntadores
		return 1;
	}
	return 0;
}

int main()  //Funcion principal que se encarga de mostrarlos datos en pantalla
{
	
	int opc=0,num,dt,res;
	pila Pila;  //Se declara la estructura para que pueda ser usada
	Pila.index=-1;  //se iguala a -1 para controlar si tiene datos
	
	do{  //Ciclo que controla el menu para repetirse multiples ocaciones como el usuario decida
		
	cout<< "\n\t~<< Menu >>~\n"<<"1.- push\n"<<"6.-Salir\n"<<"\tIngresa una opcion:"<<endl<<"\n \t"; cin>>opc;
	system("clear");
	switch(opc)
		{
		case 1:
				cout<<"\nDato a ingresar: "; cin>>num;
				if (push(&Pila, num)==1)  //La funcion se controla por medio de un condicional para ver si tiene espacio
				{
					cout<<"Dato insertado\n"<<endl;		
				}
				else
				{
					cout<<"Pila llena\n"<<endl;
				}
				
			break;
	
		case 6:
				exit;
		break;
		
		default:
				
				cout<<"\tOpcion invalida"<<endl;
				
			break;
	
		}
	}while(opc!=6);
	
	
	return 0;
}