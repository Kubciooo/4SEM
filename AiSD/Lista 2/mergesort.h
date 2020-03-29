#include <bits/stdc++.h>
using namespace std;
///przy opisach zakladam porzadek rosnacy

vector<int> t;

void merge(vector<int> &arr, int low, int p, int high, int cmp) //polacz dwie tablice
{
  int i,j,q; //zmienne pomocnicze
  for (int i=low; i<=high; i++) //przypisywanie do tablicy pomocniczej elementow z glownej tablicy
  {
    t[i]=arr[i];
  }
  i=low; j=p+1; q=low; //i zaczyna się od 0 i idzie do p, j zaczyna się od p+1 i idzie do high
  while (i<=p && j<=high) //teraz chcemy obie połączone tablice złączyć w jedną posortowaną
  {
    porownania++; //zaraz bedziemy porowynwac
    if (compare(t[i],t[j],cmp)) //jeżeli t[i] < t[j]
    {
      swapy++;
      arr[q]=t[i];
      q++;
      i++;
    }
    else
    {
      arr[q]=t[j];
      q++;
      j++;
    }
  }
  while (i<=p) //jeżeli z lewej coś zostało
  {
    arr[q] = t[i];
    q++;
    i++;
  }
  while(j <= high) //jeżeli z prawej coś zostało
  {
    arr[q] = t[j];
    q++;
    j++;
  }
}

void merges(vector<int> &arr, int low, int high, int cmp)
{
  int p;
  if (low<high)
  {
    p=(low+high)/2;
    merges(arr, low, p, cmp);    // Dzielenie lewej części
    merges(arr, p+1, high, cmp);   // Dzielenie prawej części
    merge(arr, low, p, high, cmp);   // Łączenie części lewej i prawej
  }
}
void mergesort(vector<int> &arr, int low, int high, int cmp)
{
  porownania = 0;
  swapy = 0;
  t.resize(arr.size());
  merges(arr,low,high,cmp);
}
