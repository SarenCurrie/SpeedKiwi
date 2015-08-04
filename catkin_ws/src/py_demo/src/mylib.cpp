#include "mylib.h" 

int mylib_function() 
{ 
        static int counter = 0; 
        return counter--; 
} 
