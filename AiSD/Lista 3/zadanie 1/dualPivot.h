#include <bits/stdc++.h> 
using namespace std; 
int partition(vector<int> &arr, int low, int high, int* lp, int cmp)  
{  
    porownania++;
    if (compare(arr[high],arr[low],cmp)) //lewy ma byc mniejszy od prawego cmp 
    {
        swap(arr[low], arr[high]);  
        swapy++;
    }  

      
    int j = low + 1;  //zaczynamy powyzej low 
    int g = high - 1; //z drugiej strony zaczynamy ponizej high
    int k = low + 1;  
    int p = arr[low]; //lewy pivot (kandydat) 
    int q = arr[high];  //kandydat na prawy pivot 
    while (k <= g)  
    {  
        // jezeli element jest mniejszy od lewego pivotu, 
        porownania+=2;
        if (compare(arr[k], p,cmp))
        {  
            porownania--;
            swapy++;
            swap(arr[k], arr[j]);  
            j++;  
        }  
        // if elements are greater than or equal  
        // to the right pivot  
        else if (arr[k] == q || compare(q,arr[k],cmp))
        {  
            while (compare(q,arr[g],cmp) && k < g)
            {
                g--;  
                porownania++;
            }
            swapy++;
            swap(arr[k], arr[g]);  
            g--;  
            porownania++;
            if (compare(arr[k], p,cmp))
            {  
                swapy++;
                swap(arr[k], arr[j]);  
                j++;  
            }  
        }  
        k++;  
    }  
    j--;  
    g++;  
  
    // ustawiamy pivoty.  
    swapy+=2;
    swap(arr[low], arr[j]);  
    swap(arr[high], arr[g]);  
  
    // lewy pivot ustawiamy jako j  
    *lp = j;   
  
    return g;   //prawy pivot to będzie g 
}  
  

void DualPivotQuickSort(vector<int> &arr, int low, int high, int cmp)  //wszystko na lewo od lewego pivota - mniejsze od niego, pomiedzy lewym a prawym sa mniejsze od prawego i wieksze od lewego, na prawo od prawego sa wieksze od prawego
{  
    if (low < high)  
    {  
        int p, q;  
        q = partition(arr, low, high, &p, cmp);//wyznaczamy lewy i prawy pivot 
        DualPivotQuickSort(arr, low, p- 1, cmp);  //od początku do lewego pivota -1 
        DualPivotQuickSort(arr, p + 1, q - 1,cmp);  //od lewego pivota+1 do prawego-1
        DualPivotQuickSort(arr, q+ 1, high,cmp);  // od prawego+1 do końca 
    }  
}  
  

