#include <stdio.h>
#include <stdlib.h>

#define infty 2147483647 // int is 4 bytes. (2^31-1)

typedef struct priorityqueue PriorityQueue;
struct priorityqueue
{
    int size;
    int capacity;
    int *heap;
    int *index;
    int *key;
};

typedef struct edge Edge;
struct edge
{
    int VRTX;
    int COST;
    Edge *NEXT;
};

typedef struct graph Graph;
struct graph
{
    int N;
    Edge **LIST;
    int *pred;
};

Graph *read_input();
void PRIM(Graph *, int);
void InitPQ (Graph *, PriorityQueue *, int);
int IsEmptyPQ(PriorityQueue *);
int EXTRACT_MIN (PriorityQueue *);
void HEAPIFY (PriorityQueue *, int);
void DECREASE_KEY (PriorityQueue *, int, int);
void DISPLAY_MST (Graph *);

// Utilities
void PRINT_LIST (Edge *);
void FREE_LIST (Edge *);
void FREE_GRAPH (Graph *);
void FREE_PQ (PriorityQueue *);
void PQ_UNDERFLOW();


int main()
{
    Graph *G;
    G = read_input();
    PRIM (G, 1);
    // Assume that Vertex 1 is always start vertex/root of MST
    DISPLAY_MST(G);
    
    FREE_GRAPH (G);
    
    return(0);
}

Edge *create_edge (int vrtx, int cost)
{
    Edge *temp = (Edge *) malloc (sizeof(Edge));
    temp->VRTX = vrtx;
    temp->COST = cost;
    temp->NEXT = NULL;
    return temp;
}

Graph *read_input()
{
    Graph *G = (Graph *) malloc (sizeof(Graph));
    scanf("%d", &(G->N));
    
    G->LIST = (Edge **) malloc ((G->N + 1)*sizeof(Edge *));
    
    int edge;
    Edge *end;
    int i, j;
    for (i = 1; i <= G->N; i++)
    {
        G->LIST[i] = NULL;
        for (j = 1; j <= G->N; j++)
        {
            scanf("%d", &edge);
            if (edge > 0)
            {
                if (G->LIST[i] == NULL)
                {
                    end = create_edge(j, edge);
                    G->LIST[i] = end;
                }
                else
                {
                    end->NEXT = create_edge(j, edge);
                    end = end->NEXT;
                }
            }
        }
    }
    
    G->pred = (int *) malloc ((G->N + 1)*sizeof(int));
    
    return G;
}

void PRIM (Graph *G, int s)
{
	//Implement this function
    return;
}

void InitPQ (Graph *G, PriorityQueue *PQ, int s)
{
	//Implement this function
    return;
}

int IsEmptyPQ (PriorityQueue *PQ)
{
    return PQ->size == 0;
}

int EXTRACT_MIN (PriorityQueue *PQ)
{
	//Implement this function  
    return j;
}

void HEAPIFY (PriorityQueue *PQ, int r)
{
	//Implement this function
    return;
}

void DECREASE_KEY (PriorityQueue *PQ, int l, int newkey)
{
	//Implement this function
    return;
}

void DISPLAY_MST (Graph *G)
{
    int TCost = 0;
    int l, j;
    for (l = 1; l <= G->N; l++)
    {
        if (G->pred[l] != 0)
        {
            Edge *alpha = G->LIST[l];
            while (alpha != NULL)
            {
                j = alpha->VRTX;
                if (G->pred[l] == j)
                {
                    printf ("(%d, %d) -- %d\n", l, j, alpha->COST);
                    TCost = TCost + alpha->COST;                    
                }
                alpha = alpha->NEXT;
            }
        }
    }
    printf("%d\n", TCost);
    return;
}


////
// Utilities Section
////

void PRINT_LIST (Edge *start)
{
    Edge *current = start;
    while (current != NULL)
    {
        printf("(%d:%d) -> ", current->VRTX, current->COST);
        current = current->NEXT;
    }
    
    return;
}

/**
Deallocates a linked list
**/
void FREE_LIST (Edge *start)
{
    Edge *current, *obsolete;
    current = start;
    while (current != NULL)
    {
        obsolete = current;
        current = current->NEXT;
        free(obsolete);
    }
    return;
}

void FREE_GRAPH (Graph *G)
{
    int i;
    for (i = 1; i <= G->N; i++) FREE_LIST (G->LIST[i]);
    free (G->pred);
    free (G);
}

void FREE_PQ (PriorityQueue *PQ)
{
    free(PQ->heap);
    free(PQ->index);
    free(PQ->key);
    free (PQ);
}

void PQ_UNDERFLOW(void)
{
    printf("Priority Queue underflow detected.\n");
    exit(1);
}




















