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

int pop(pila *Pila) //Funcion de tipo entero que es encargado de eliminar elementos del arreglo
{
	int aux; //Variable que es usada como ancla y almacena el dato que se eliminara
	if(EvitarUnder(*Pila)==0)
	{
		aux=Pila->items[Pila->index];
		Pila->items[Pila->index]=0;
		Pila->index--;
		return aux;
	}
	return 0;
}

void Peek(pila *Pila) //Funcion que contrala la operacion llamada Peek y retornal el valor del tope de la pila
{
	cout<<"\n"<<Pila->items[Pila->index]<<endl;

}

void Peekall(pila *Pila) //Funcion que muestra todos los datos que contiene la pila
{  
	for (int tope=4;tope>=0;tope--) //Un ciclo que recorre todos los elementos y los imprime uno por uno
	{
            cout<<"\n"<<tope<<":"<<Pila->items[tope]<<endl;
	}
   
}

int PeekIndex(pila *Pila, int dato1) //Funcion que recibe como parametro un tipo de dato entero 
{
	int z=-1; //Variable que almacenara el indice donde se encuentra el valor
	for (int tope=0;tope<5;tope++) //Ciclo que recorre todos los elementos
	{
	    if(Pila->items[tope]==dato1){ //Condicional que compara los datos que existen en la pila con el valor deseado
          z=tope; //Se almacena el indice 
         }

	}
	return z; //Regresa el indice para poder usarlo en la funcion main
		
}

int main()
{
	int opc=0,num,dt,res;
	pila Pila;  //Se declara la estructura para que pueda ser usada
	Pila.index=-1;  //se iguala a -1 para controlar si tiene datos
	
	do{ //Ciclo que controla el menu para repetirse multiples ocaciones como el usuario decida
		
	cout<< "\n\t~<< Menu >>~\n"<<"1.- push\n"<<"2.- Peek\n"<<"3.- Peekall\n"<<"4.- Peek por index\n"<<"5.- Pop\n"<<"6.- Salir\n"<<"\tIngresa una opcion:"<<endl<<"\n \t"; cin>>opc;
	system("clear"); //Linea para borrar pantalla
	switch(opc)
		{

		case 1: //Controla el metodo push 

				cout<<"\nDato a ingresar: "; cin>>num;
				if (push(&Pila, num)==1)
				{
					cout<<"Dato insertado\n"<<endl;		
				}
				else
				{
					cout<<"Pila llena\n"<<endl;
				}
				
			break;
		case 2: //Controla el metodo peek 
			
			if(num!=0)
			{
				Peek(&Pila);
			}
			else
			{
				cout<<"\nPila vacia"<<endl;
			}
				
			break;
		case 3: //Controla la funcion que muestra todos los datos
				Peekall(&Pila);
			break;
		case 4: //Controla la funcion PeekIndex para que el usuario busque algun dato
				
				cout<<"\nDato a buscar: "; cin>>dt;
				res = PeekIndex(&Pila, dt);
				
				if(res!=-1){
					cout<<"Dato: "<<dt<<endl<<"Posicion: "<<res<<endl;
				}
				else{
					cout<<"No existe dato"<<endl;
				}
		break;
		case 5: //Controla la funcion pop para eliminar datos de la pila
				num=pop(&Pila);
				if(num!=0)
				{
					cout<<"\nElemento eliminado: "<<num<<"\n";
				}
				else
				{
					cout<<"\nPila vacia"<<endl;
				}
			
		break;
		
		case 6: //Controla la salida del documento
				exit;
		break;
		
		default: //Controla que el usuario no ingrese una opcion del menu incorrecta
				
				cout<<"\tOpcion invalida"<<endl;
				
			break;
	
		}
}while(opc!=6);
	

	return 0;
}
