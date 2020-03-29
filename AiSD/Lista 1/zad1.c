#include<stdio.h>
#include<stdlib.h>

#define q_MAX 1000001

struct FIFO
{
    int start, end, size; /// start->poczatek, end->koniec, size->wielkosc
    int *values; ///tablica z wartosciami na kolejce
};

void push_back(struct FIFO *queue, int value) ///dodanie wartosci na koniec kolejki
{
    if(queue->size == q_MAX){
        printf("kolejka zapelniona!\n");
        return;
    }
    queue->end = (queue->end + 1)%q_MAX; ///przesuwamy koniec o 1 punkt dalej, ale %q_MAX bo chcemy po dodaniu pierwszego elementu miec end = 0
    (queue->size)++;    ///teraz wielkosc kolejki sie zwieksza
    queue->values[queue->end] = value; ///dodajemy wartosc na koniec
}
int pop_front(struct FIFO *queue) ///wyrzucenie z kolejki
{
    if(queue->size == 0)return 0;
    int value = queue->values[queue->start];
    (queue->start) = (queue->start+1)%q_MAX;
    (queue->size)--;
    return value;
}
int getFront(struct FIFO *queue){
    if(queue->size != 0)return queue->values[queue->start];
    return 0;
}
int getEnd(struct FIFO *queue){
    if(queue->size !=0)return queue->values[queue->end];
    return 0;
}
int main()
{
    struct FIFO *queue = malloc(sizeof(struct FIFO));
    queue->start = 0;
    queue->end = q_MAX -1;
    queue->size = 0;
    queue->values = calloc(q_MAX,sizeof(int));
    push_back(queue,1);
    push_back(queue,2);
    push_back(queue,3);
    push_back(queue,4);
    push_back(queue,3);
    printf("Na poczatku kolejki stoi %d, a na koncu %d\n",getFront(queue),getEnd(queue));
    printf("%d wyszedl z kolejki, teraz na poczatku stoi ",pop_front(queue));
    printf("%d\n ",getFront(queue));


    return 0;
}
