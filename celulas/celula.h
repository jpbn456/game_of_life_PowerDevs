//HeadersDir:stdio
//CPP:celulas/celula.cpp
#if !defined celula_h
#define celula_h

#include "simulator.h"
#include "event.h"
#include "stdarg.h"

#include "iostream"


class celula: public Simulator { 
// Declare the state,
// output variables
// and parameters
double sigma;
bool alive;
int xPos;
int yPos;
int aliveNeighbors;
#define INF 1e20
public:
	celula(const char *n): Simulator(n) {};
	void init(double, ...);
	double ta(double t);
	void dint(double);
	void dext(Event , double );
	Event lambda(double);
	void exit();
};
#endif
