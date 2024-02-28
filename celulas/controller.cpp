#include "controller.h"
void controller::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.
va_list parameters;
va_start(parameters,t);
//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type
sigma = 0;
int fvar = va_arg(parameters,int);
n = fvar;
fvar = va_arg(parameters,int);
m = fvar;

}
double controller::ta(double t) {
//This function returns a double.
return sigma+1;
}
void controller::dint(double t) {
if(sigma = 0)
	sigma = INF;
}
void controller::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition
//TO DO: Informar a todos los vecinos que cambió el estado a uno nuevo
int* value = (int*)x.value;
x_cell = value[0];
y_cell = value[1];
alive_cell = value[2];
sigma = 0;
}
Event controller::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)
/*int calculateCellPort(int x,int y){
		return ((x*(m-1))+y)*-/ 
*/

int result[3];
result[0] = x_cell;
result[1] = y_cell;
result[2] = alive_cell;
return Event(&result,0);
}
void controller::exit() {
//Code executed at the end of the simulation.

}
