#include "celula.h"
void celula::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.//
va_list parameters;
va_start(parameters,t);
//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type
sigma = 0;
int fvar = va_arg(parameters,int);
xPos = fvar;
fvar = va_arg(parameters,int);
yPos = fvar; 
fvar = va_arg(parameters,int);
alive = fvar;
aliveNeighbors = 0;


}
double celula::ta(double t) {
//This function returns a double.
return sigma+1; //std::numeric_limits<double>::infinity();
}
void celula::dint(double t) {
if(sigma = 0) 
	sigma = INF;
}
void celula::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition
int* values = (int*)x.value;
if(
	(values[0] == xPos-1 && values[1] == yPos)
	||(values[0] == xPos+1 && values[1] == yPos)
	||(values[0] == xPos && values[1] == yPos-1)
	||(values[0] == xPos-1 && values[1] == yPos-1)
	||(values[0] == xPos+1 && values[1] == yPos-1)
	||(values[0] == xPos && values[1] == yPos+1)	
	||(values[0] == xPos-1 && values[1] == yPos+1)
	||(values[0] == xPos+1 && values[1] == yPos+1)
	){
		if(values[2] == 0) 
			 aliveNeighbors--;
		else 
			 aliveNeighbors++; 
		if( aliveNeighbors == 3 && alive == 0) 
			alive = 1;
		else 
			if ((aliveNeighbors == 2 || aliveNeighbors == 3) && alive == 1)
			alive = 1;
		else 
			alive = 0;
		sigma = 0;
	}
else 
	sigma = INF;


}
Event celula::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)

int value[3];
value[0] = xPos;
value[1] = yPos;
value[2] = alive;
return Event(&value,0);
}
void celula::exit() {
//Code executed at the end of the simulation.

}
