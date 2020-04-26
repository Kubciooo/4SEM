#include <bits/stdc++.h>
using namespace std;


int partition(vector<int> &array, int low, int high, int cmp)  //chcemy podzielić tablicę na dwie - w jednej będą elementy większe od pivota, w drugiej mniejsze
{
  int pivot = array[high]; //pivot to element, na podstawie ktorego tworzymy te 2 tablice
  int i = (low - 1);

  for (int j = low; j < high; j++) // przechodzimy po całej tablicy (to nie jest cała tablica wynikowa, tylko cała część, którą teraz chcemy posortować
  {
        porownania++;
    if (compare(array[j], pivot, cmp))
    {
      i++;
      swapy++;
      swap(array[i], array[j]);
    }
  }
  swapy++;
  swap(array[i + 1], array[high]); //pivot w tym miejscu powinien być, czyli array[i+1] jest uporządkowana
  return (i + 1); //to miejsce już jest na swoim miejscu na pewno
}
void quickSort(vector<int> &array, int low, int high, int cmp)
{
  if (low < high)
  {
    int pi = partition(array, low, high, cmp);
    quickSort(array, low, pi - 1, cmp);
    quickSort(array, pi + 1, high, cmp);
  }
}
