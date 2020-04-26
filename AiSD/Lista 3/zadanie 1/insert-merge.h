#include<bits/stdc++.h>
using namespace std;


template<class T>
bool comparator(T a, T b, char* plik)  //funkcja porównująca
{
        int i = 0;
        string p = plik;
        string x = "<=";
        string d = ">=";
        if(p[0] == '<') return a < b;
        if(p[0] == '>') return a > b;
        fstream f;
        f.open(plik, ios::in); 
        T c;
        
        while(f >> c)
        {
                if(c == a) return true;
                if(c == b) return false;
        }
        return false;
}

template <class T>

void insertSort2(T arr[], char* comp, int from, int to)
{
  for(int i=from + 1; i<=to; i++)
  {
    T temp=arr[i];
    int j=i-1;
    porownania++;
    while(comparator(temp,arr[j],comp) && (j>=from))
    {
      porownania++;
      swapy++;
      arr[j+1]=arr[j];
      j=j-1;
    }
    arr[j+1]=temp;
  }
}

template <class T>
void merge2(T arr[], int low, int p, int high, char* cmp) //polacz dwie tablice
{
          T t2[high+1];
          int i,j,q; //zmienne pomocnicze
          for (int i=low; i<=high; i++) //przypisywanie do tablicy pomocniczej elementow z glownej tablicy
          {
            t2[i]=arr[i];
          }
          i=low; j=p+1; q=low; //i zaczyna się od 0 i idzie do p, j zaczyna się od p+1 i idzie do high
          while (i<=p && j<=high) //teraz chcemy obie połączone tablice złączyć w jedną posortowaną
          {
            porownania++; //zaraz bedziemy porowynwac
            if (comparator(t2[i],t2[j],cmp)) //jeżeli t[i] < t[j]
            {
              swapy++;
              arr[q]=t2[i];
              q++;
              i++;
            }
            else
            {
              arr[q]=t2[j];
              q++;
              j++;
            }
          }
          while (i<=p) //jeżeli z lewej coś zostało
          {
            arr[q] = t2[i];
            q++;
            i++;
          }
        while(j <= high) //jeżeli z prawej coś zostało
        {
           arr[q] = t2[j];
           q++;
           j++;
        }
}
template <class T>
void merges2(int MAX, T arr[], int low, int high, char* cmp)
{
  int p;
 
  if (low<high)
  {
    if(high-low < MAX)
    {           
            insertSort2(arr,cmp,low,high);
    }
    else
    {
            p=(low+high)/2;
            merges2(MAX,arr, low, p, cmp);    // Dzielenie lewej części
            merges2(MAX,arr, p+1, high, cmp);   // Dzielenie prawej części
            merge2(arr, low, p, high, cmp);   // Łączenie części lewej i prawej
    }
  }
}
template <class T>
void mergesort2(int MAX, T arr[], int low, int high, char* cmp)
{
  porownania = 0;
  swapy = 0;
  merges2(MAX, arr,low,high,cmp);
}
