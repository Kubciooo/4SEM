#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
typedef struct node node;

struct node ///lista
{
    int value; ///wartosc
    node *next; ///wskaznik na kolejny element
};
int getRandom(int min, int max) ///wez losowa liczbe od min do max
{
    int tmp;
    if (max>=min)
        max-= min;
    else
    {
        tmp= min - max;
        min= max;
        max= tmp;
    }
    return max ? (rand() % max + min) : min;
}
void add (int x, node * list) ///dodaj na liste
{
    if (list->value == NULL)
    {
        list->value = x;
        return;
    }
    node *temp = list;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    node *new = malloc (sizeof (node *));
    new->next = NULL;
    new->value = x;
    temp->next = new;
}
bool isEmpty(node * list)  ///czy lista jest pusta
{
    if(list->value == NULL)
        return true;
}
void find (int x, node * list) ///znajdz element na liscie
{
    int pos = 1;
    node *temp = list;
    while (temp->next != NULL && temp->value != x)
    {
        temp = temp->next;
        pos++;
    }
    if (temp->value == x)
    {
        // printf ("found at position %d\n", pos);
    }
    //else
    // printf ("didn't find!\n");
}
void findRandom(node * list) ///znajdz losowy element
{
    int x = getRandom(1,2000);
    find(x,list);
}
void printList(node * list) ///wypisz liste
{
    node *temp = list;
    while(temp->next != NULL)
    {
        printf("%d ", temp->value);
        temp = temp->next;
    }
    if(!isEmpty(list))
        printf("%d\n", temp->value);
}

node * merge(node * list1, node * list2) ///merge list
{
    node * newList = malloc(sizeof(node));
    node *temp = list1;
    while(temp->next != NULL)
    {
        int val = temp->value;
        temp = temp->next;
        add(val, newList);
    }
    if(!isEmpty(list1))
    {
        add(temp->value, newList);
    }
    node *temp2 = list2;
    while(temp2->next != NULL)
    {
        int val = temp2->value;
        temp2 = temp2->next;
        add(val, newList);

    }
    if(!isEmpty(list2))
    {
        add(temp2->value, newList);
    }
    return newList;
}
int main ()
{
    srand(time(NULL));
    node *list = malloc (sizeof (node));
    list->value = NULL;
    list->next = NULL;
    node *list2 = malloc(sizeof(node));
    list2->value = NULL;
    list2->next = NULL;
    node *list3 = malloc(sizeof(node));
    list3->value = NULL;
    list3->next = NULL;
    for(int i = 0; i<1000; i++)
    {
        int randomNumber = getRandom(1,2000);
        add(randomNumber, list);
    }

    /** merge list **/
    printf("merge list: \n");
    for(int i = 0; i<10; i++)
    {
        int randomNumber = getRandom(1,50);
        add(randomNumber, list2);
    }
    for(int i = 0; i<10; i++)
    {
        int randomNumber = getRandom(1,50);
        add(randomNumber, list3);
    }
    printList(list2);
    printList(list3);
    node * newList = merge(list2,list3);
    printList(newList);
    printf("\n\n\n");

    /** liczenie sredniej wartosc **/
    int value = getRandom(1,2000);
    clock_t t;
    t = clock();
    for(int i = 0; i<1000000; i++)
    {
        find(value, list);
    }
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("znalezienie tego samego elementu milion razy zajelo %.10f sekund\n Daje to srednio %.10f sekund na element\n", time_taken, time_taken/1000000);
    t = clock();
    for(int i = 0; i<1000000; i++)
    {
        findRandom(list);
    }
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("znalezienie losowego elementu milion razy zajelo %.10f sekund\n Daje to srednio %.10f sekund na element", time_taken, time_taken/1000000);
    return 0;
}


