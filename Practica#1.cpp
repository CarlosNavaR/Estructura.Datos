/*

Nava Reyes Carlos - 17212163

Desplegar los primeros 100 numeros naturales
Reglas: 
	-No utilizar iteradores 
Unfold the first 100 natural numbers
Rules: 
	-Don't use iterators
	
*/
#include <iostream>
using namespace std;	

int Numero(int x) //Funcion
{	cout<<x<<"\n";
	if (x<100)
	{
		return Numero(x+1);
	}
}

int main()
{
	
	Numero(1);
	
	return 0;
}