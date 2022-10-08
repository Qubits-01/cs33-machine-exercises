#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define newline printf("\n")

typedef int BinaryTreeDataType;
typedef struct binarytreenode BinaryTreeNode;
struct binarytreenode
{
    int LTAG;
    BinaryTreeNode *LSON;
    BinaryTreeDataType DATA;
    BinaryTreeNode *RSON;
    int RTAG;
};


struct edge
{
	int name;
    int lson;
    int rson;
};
typedef struct edge Edge;

void CREATE(BinaryTreeNode **);
void POSTORDER_T (BinaryTreeNode *);
void PREORDER_T (BinaryTreeNode *);
void INORDER_T (BinaryTreeNode *);
BinaryTreeNode *INSUC(BinaryTreeNode *);
BinaryTreeNode *INPRED(BinaryTreeNode *);
BinaryTreeNode *PRESUC(BinaryTreeNode *);
BinaryTreeNode *POSTSUC(BinaryTreeNode *);
void VISIT (BinaryTreeNode *);
void FREE_TREE (BinaryTreeNode *);
int read_tree_input(Edge **, int **);
int LOOK (int *, int, int);

BinaryTreeNode *create_node(BinaryTreeDataType);

int main()
{
    BinaryTreeNode *H;
    
    CREATE(&H);
    INORDER_T(H);
    newline;
    PREORDER_T(H);
    newline;
    POSTORDER_T (H);
    newline;
    
    FREE_TREE(H->LSON);
    free(H);
    return 0;
}

int read_tree_input (Edge **edges, int **inorder_list)
{
	int i, n;
    int lson, rson, name;
	
	scanf("%d\n", &n);
    *edges = (Edge *) malloc (n*sizeof(Edge));
    for (i = 0; i < n; i++)
    {
        (*edges)[i].name = i+1;
        
        scanf("%d %d\n", &lson, &rson);
        (*edges)[i].lson = lson;
        (*edges)[i].rson = rson;
    }
    *inorder_list = (int *) malloc (n*sizeof(int));
    for (i = 0; i < n; i++)
    {
        scanf("-%d-", &name);
        (*inorder_list)[i] = name;
    }
	
	return n;
}

void CREATE (BinaryTreeNode **H)
{
	Edge *edges;
    int *inorder_list;
    BinaryTreeNode **nodes;
    BinaryTreeNode *head;
	int n;
	int i = 0, index;
	
	n = read_tree_input(&edges, &inorder_list);
    
    /**
    Head node of the threaded binary tree.
    **/
    head = (BinaryTreeNode *) malloc (sizeof(BinaryTreeNode));
    head->DATA = -1;
    head->RSON = head;
    head->RTAG = 1;
	
    nodes = (BinaryTreeNode **) malloc (n*sizeof(BinaryTreeNode*));
	for (i = 0; i < n; i++)
    {
        nodes[i] = (BinaryTreeNode *) malloc (sizeof(BinaryTreeNode));
        nodes[i]->DATA = edges[i].name;
        nodes[i]->LSON = NULL;
        nodes[i]->LTAG = 0;
        nodes[i]->RSON = NULL;
        nodes[i]->RTAG = 0;
    }
    
    head->LSON = nodes[0];
    head->LTAG = 1;
    
    /*
    Creates the regular and thread links
    */
    for (i = 0; i < n; i++)
    {
        
        if (edges[i].lson > 0) 
        {
            nodes[i]->LSON = nodes[edges[i].lson-1];
            nodes[i]->LTAG = 1;
        }
        else
        {
            index = LOOK (inorder_list, n, edges[i].name);
            if (index == 0) nodes[i]->LSON = head;
            else nodes[i]->LSON = nodes[inorder_list[index-1]-1];
        }
        
        if (edges[i].rson > 0) 
        {
            nodes[i]->RSON = nodes[edges[i].rson-1];
            nodes[i]->RTAG = 1;
        }
        else
        {
            index = LOOK (inorder_list, n, edges[i].name);
            if (index == n-1) nodes[i]->RSON = head;
            else nodes[i]->RSON = nodes[inorder_list[index+1]-1];
        }
        
    }
    
    *H = head;
	
	free(edges);
    free(inorder_list);
}

void VISIT(BinaryTreeNode *T)
{
    printf("-%d-", T->DATA);
}

/**
Deallocating a Binary Tree should be
done in POSTORDER. Suggested is iterative
to avoid stack overflow.
**/
void FREE_TREE (BinaryTreeNode *H)
{
    if (H->LTAG == 1) FREE_TREE(H->LSON);
    if (H->RTAG == 1) FREE_TREE(H->RSON);    
    free(H);
    
    return;
}

/*
Standard linear search
*/
int LOOK (int *list, int size, int key)
{
    int i;
    for (i = 0; i < size; i++)
        if (list[i] == key) return i;
    
    return -1;
}

// Traversals Onward
BinaryTreeNode *INSUC(BinaryTreeNode *alpha)
{
    // implement this
}

BinaryTreeNode *INPRED (BinaryTreeNode *alpha)
{
    // implement this
}

void INORDER_T (BinaryTreeNode *H)
{
    // implement this
}

BinaryTreeNode *PRESUC (BinaryTreeNode *alpha)
{
    // implement this
}

void PREORDER_T (BinaryTreeNode *H)
{
    // implement this
}

BinaryTreeNode *POSTSUC (BinaryTreeNode *alpha)
{
    // implement this
    
}

void POSTORDER_T (BinaryTreeNode *H)
{
    // implement this
}



