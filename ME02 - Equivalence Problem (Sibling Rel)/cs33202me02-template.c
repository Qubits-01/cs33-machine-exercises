/**
For this code template, you may change the
function bodies as you see fit, except for
the main function.
**/

#include <stdio.h>
#include <stdlib.h>

#define newline printf("\n")

void EQUIVALENCE (void);
int* INIT_ARRAY (int);
int NUM_EQUI_CLASSES(void);
/**
The following are optional functions. 
The use of this functions depends on how you would like to implement EQUIVALENCE

void UNION (int, int);
int FIND (int);
**/

/**
QUIWA book suggested that the FATHER
array be declared as global for easier
implementation of the codes.
**/
// Declare global variables here
int *FATHER; //the global FATHER array
int SIZE; //the global FATHER array size
// Declare global variables here

int main()
{   
    EQUIVALENCE ();
    printf("%d", NUM_EQUI_CLASSES());
    
    free (FATHER);
    return 0;
}

void EQUIVALENCE ()
{
    int i, j, n;
    
    // get size of S
    scanf("%d\n", &n);
    
    /*
    //Initialize FATHER array
    */
    scanf("%d %d\n", &i, &j);
    while (i != 0 && j != 0)
    {
        /*
        Implement the equivalence pseudocode of Quiwa Book of your choice. 
	You may need to create and call FIND and UNION functions.
        */
        scanf("%d %d\n", &i, &j);
    }
    
    return;
}

int *INIT_ARRAY (int size)
{
    
}


int NUM_EQUI_CLASSES()
{
	int numEquiClasses=0;
	
	/**
	Determine the number of equivalence classes.
	Store it in numEquiClasses variable.
	**/

	return numEquiClasses;
}













