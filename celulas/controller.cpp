#include "controller.h"
void controller::init(double t,...) {
//The 'parameters' variable contains the parameters transferred from the editor.
va_list parameters;
va_start(parameters,t);
//To get a parameter: %Name% = va_arg(parameters,%Type%)
//where:
//      %Name% is the parameter name
//	%Type% is the parameter type
sigma = INF;
char *fvar = va_arg(parameters,char*);
m = getScilabVar(fvar); 
fvar = va_arg(parameters,char*);
n = getScilabVar(fvar);
cell_change_counter = n*m;
alive_cells = new int*[n];
steps = 0;
fvar = va_arg(parameters, char*);
F_Name = fvar;


for(int i = 0;i < n; i++){
	alive_cells[i] = new int[m];
	for(int j = 0; j < m; j++){
		alive_cells[i][j] = 0;
	}
}

char buf[1024];
long int FOutput =  PDFileOpen(F_Name, 'w');
sprintf(buf,"step,i,j\n");
PDFileWrite(FOutput,buf,strlen(buf));
PDFileClose(FOutput);

}
double controller::ta(double t) {
//This function returns a double.
return sigma;
}
void controller::dint(double t) {
cell_change_counter = n*m;
sigma = INF;

}
void controller::dext(Event x, double t) {
//The input event is in the 'x' variable.
//where:
//     'x.value' is the value (pointer to void)
//     'x.port' is the port number
//     'e' is the time elapsed since last transition

int *value = (int*)x.value;
int x_pos = value[0];
int y_pos = value[1];
int alive = value[2];

alive_cells[x_pos][y_pos] = alive;
cell_change_counter-=1;
sigma -= e;
if(cell_change_counter == 0){
	sigma = 0;
}
}
Event controller::lambda(double t) {
//This function returns an Event:
//     Event(%&Value%, %NroPort%)
//where:
//     %&Value% points to the variable which contains the value.
//     %NroPort% is the port number (from 0 to n-1)

result[0] = static_cast<void*>(alive_cells);
int* pN = new int(n); 
int* pM = new int(m);

char buf[1024];
long int FOutput = PDFileOpen(F_Name, 'a');
if(steps < 2000){
	steps++;
	result[1] = static_cast<void*>(pN);
	result[2] = static_cast<void*>(pM);
	for(int i = 0; i < n; ++i) {
    	for(int j = 0; j < m; j++) {
			if(alive_cells[i][j] == 1){
        	sprintf(buf,"%d,%d,%d\n",steps,i,j);
				PDFileWrite(FOutput,buf,strlen(buf));
			}
		}
	}
}
PDFileClose(FOutput);

return Event(&result,0); 

}
void controller::exit() {
//Code executed at the end of the simulation.

}
