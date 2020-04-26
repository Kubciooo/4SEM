#include<bits/stdc++.h>
using namespace std;

void insertSort(vector<int> &arr, int comp)
{
  for(int i=0; i<arr.size(); i++)
  {
    int temp=arr[i];
    int j=i-1;
    porownania++;
    while(compare(temp,arr[j],comp) && (j>=0))
    {
      porownania++;
      swapy++;
      arr[j+1]=arr[j];
      j=j-1;
    }
    arr[j+1]=temp;
  }
}
