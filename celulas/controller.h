//CPP:celulas/controller.cpp
#if !defined controller_h
#define controller_h

#include "simulator.h"
#include "event.h"
#include "stdarg.h"



class controller: public Simulator { 
// Declare the state,
// output variables
// and parameters
double sigma;
int n;
int m;
int x_cell;
int y_cell;
bool alive_cell;
#define INF 1e20

public:
	controller(const char *n): Simulator(n) {};
	void init(double, ...);
	double ta(double t);
	void dint(double);
	void dext(Event , double );
	Event lambda(double);
	void exit();
};
#endif
