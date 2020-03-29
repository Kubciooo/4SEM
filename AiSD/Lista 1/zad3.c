#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
typedef struct node node;

struct node ///lista
{
    int value; ///wartosc
    node *next; ///wskaznik na kolejny element
    node *prev; /// poprzedni element
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
bool isEmpty(node* list) ///czy list ajest pusta?
{
    return list->value == NULL;
}
node * push_back(int item, node* head) ///dodaj na koniec
{
    if(isEmpty(head))
    {
        head->value = item;
        head->next = head;
        head->prev = head;
        return;
    }
    node* newNode = malloc(sizeof(node));
    newNode->value = item;
    newNode->next = head;
    newNode->prev = head->prev;
    head->prev->next = newNode;
    head->prev = newNode;
    return head;
}
node * push_front(int item, node * head) /// dodaj na poczatek
{
    push_back(item, head);
    return head->prev;
}
void printList(node * head) ///wypisz liste
{
    node* temp = head;
    if(temp->next == head)
    {
        printf("%d\n",temp->value);
        return;
    }
    printf("%d ", temp->value);
    temp = temp->next;
    while(temp != head)
    {
        printf("%d ",temp->value);
        temp = temp->next;
    }
    printf("\n");
}
node * pop_back(node * head) ///usun z konca
{
    if(head->prev == head)
    {
        head->value = NULL;
        return head;
    }
    node * del = head->prev;

    head->prev = del->prev;
    del->prev->next = head;
    return head;
}
node * pop_front(node * head)
{
    node * temp = head->next;
    pop_back(head->next);
    return temp;

}
node * merge(node * list1, node * list2) ///usun z poczatku
{
    node * newList = malloc(sizeof(node));
    newList->value = NULL;
    newList->next = newList;
    newList->prev = newList;
    while(!isEmpty(list1))
    {
        newList = push_back(list1->value, newList);
        list1 = pop_front(list1);
    }
    while(!isEmpty(list2))
    {
        newList = push_back(list2->value, newList);
        list2 = pop_front(list2);
    }
    return newList;
}

int find(node * head, int value) ///znajdz element
{
    node * temp = head;
    int pos = 1;
    if(head->value==value)
        return 0;
    do
    {
        temp = temp->next;
        if(temp->value == value)
        {
            return pos; ///znaleziono wartosc
        }
        pos++;
    }
    while(temp->next != head);


    return -1;
}

void findRandom(node * head) ///znajdz losowy element
{
    int x = getRandom(1,2000);
    find(head,x);
}

int main ()
{
    srand(time(NULL));
    node *list = malloc (sizeof (node));
    list->value = NULL;
    list->next = list;
    list->prev = list;
    for(int i = 0; i<1000; i++)
    {
        int randomNumber = getRandom(1,2000);
        push_back(randomNumber, list);
    }
    int value = getRandom(1,2000);
    clock_t t;
    t = clock();
    for(int i = 0; i<1000000; i++)
    {
        find(list,value);
    }
    t = clock() - t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("znalezienie tego samego elementu milion razy zajelo %.10f sekund\n Daje to srednio %.10f ms na element\n", time_taken, time_taken/10000);
    t = clock();
     for(int i = 0; i<1000000; i++)
    {
        findRandom(list);
    }
    t = clock() - t;
     time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("znalezienie losowego elementu milion razy zajelo %.10f sekund\n Daje to srednio %.10f ms na element\n", time_taken, time_taken/10000);


    /* testowanie merge */
    printf("\n merge list:\n");
    node * lista = malloc(sizeof(node));
    lista->value = NULL;
    lista->next = lista;
    lista->prev = lista;
    lista = push_back(10,lista);
    lista = push_back(20,lista);
    lista = push_back(30,lista);
    lista = push_back(40,lista);
    lista = push_back(50,lista);

    node * lista2 = malloc(sizeof(node));
    lista2->value = NULL;
    lista2->next = lista2;
    lista2->prev = lista2;
    lista2 = push_back(1,lista2);
    lista2 = push_back(2,lista2);
    lista2 = push_back(3,lista2);
    lista2 = push_back(4,lista2);
    lista2 = push_back(5,lista2);

    printList(lista);
    printList(lista2);

    node * merged = merge(lista,lista2);
    printList(merged);
    return 0;
}


