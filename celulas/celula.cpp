#include "celula.h"
void celula::init(double t,...) {
#include <iostream> // or any other standard header you might be using
using namespace std;
#include <vector>

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
// Assume x.value is initially set up correctly as described above

void* generalPointer = x.value; 
void** resultArray = static_cast<void**>(generalPointer);
int** retrievedMatrix = static_cast<int**>(resultArray[0]);
int* nPtr = static_cast<int*>(resultArray[1]); 
int* mPtr = static_cast<int*>(resultArray[2]); 
int n = *nPtr;
int m = *mPtr; // Dereference to get m
int matrix[n][m];


for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
        matrix[i][j] = retrievedMatrix[i][j];
    }
}

int alive_neighbors = 0;

m--;
n--;
if(x_pos > 0 && y_pos > 0)
	 if(matrix[x_pos-1][y_pos-1]==1)
		alive_neighbors++;
if(x_pos < n && y_pos < m)
	if(matrix[x_pos+1][y_pos+1]==1)
		alive_neighbors++;
if(x_pos < n && y_pos > 0)
	if(matrix[x_pos+1][y_pos-1]==1)
		alive_neighbors++;
if(x_pos > 0 && y_pos < m)
 	if(matrix[x_pos-1][y_pos+1]==1)
		alive_neighbors++;
if(y_pos > 0) 
	if(matrix[x_pos][y_pos-1]==1)
		alive_neighbors++;
if(y_pos < m) 
	if(matrix[x_pos][y_pos+1]==1)
		alive_neighbors++;
if(x_pos < n) 
	if(matrix[x_pos+1][y_pos]==1)
		alive_neighbors++;
if(x_pos > 0)
	if(matrix[x_pos-1][y_pos]==1)
		alive_neighbors++;

if(alive_neighbors == 3 && alive == 0) 
	alive = 1;	
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
