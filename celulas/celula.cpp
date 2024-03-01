#include "celula.h"
void celula::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.//
va_list parameters;
va_start(parameters,t);
//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type

char *fvar = va_arg(parameters,char*);
x_pos = getScilabVar(fvar);            // random seed
fvar = va_arg(parameters,char*);
y_pos = getScilabVar(fvar);
fvar = va_arg(parameters,char*);
alive = getScilabVar(fvar);
value[0] = x_pos;
value[1] = y_pos;
value[2] = alive;
sigma = 0;

}
double celula::ta(double t) {
//This function returns a double.
return sigma;
}
void celula::dint(double t) {
sigma = INF;
}
void celula::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition
int *values = (int*)x.value;
int n = (int)*(x.value[1]);
int m = (int)*x.value[2];
bool** alive_matrix = new bool*[n];
for(int i = 0; i < n; ++i) {
    alive_matrix[i] = new bool[m];
}

int alive_neighbors = 0;
for(int i = 0; i < n; ++i) 
   for(int j = 0; j < m; ++j) 
		alive_matrix[i][j] = values[2 + i * m + j] != 0;
	
if(x_pos > 0) {
	if(alive_matrix[x_pos-1][y_pos] > 0)
		alive_neighbors++; 
	if(y_pos > 0)
    if(alive_matrix[x_pos-1][y_pos-1])
      alive_neighbors++;
  if(y_pos < m-1)
    if(alive_matrix[x_pos-1][y_pos+1])
      alive_neighbors++; 
}
if(x_pos < n-1){ 
  if(alive_matrix[x_pos+1][y_pos] > 0)
    alive_neighbors++;
  if(y_pos > 0)
    if(alive_matrix[x_pos+1][y_pos-1] > 0)
      alive_neighbors++;
  if(y_pos < m-1) 
    if(alive_matrix[x_pos+1][y_pos+1] > 0) 
      alive_neighbors++;
}
if(y_pos < m-1){
  if(alive_matrix[x_pos][y_pos+1] > 0)
    alive_neighbors++;
}
if(y_pos > 0)
  if(alive_matrix[x_pos][y_pos-1] > 0)
    alive_neighbors++;
if(alive_neighbors == 3 && alive == 0) 
	alive = 1;	
else 
	if((alive_neighbors < 2 || alive_neighbors > 3) && alive == 1)
		alive = 0;
sigma = 0;



}
Event celula::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)

value[0] = x_pos;
value[1] = y_pos;
value[2] = alive;
return Event(&value,0);
}
void celula::exit() {
//Code executed at the end of the simulation.

}
