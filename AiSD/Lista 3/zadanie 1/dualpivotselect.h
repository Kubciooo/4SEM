
int partition_d(int arr[], int low, int high, int pi1, int pi2, int *lp)
{

    int i1, j1; 
    for (i1=low; i1<high; i1++)
    {
        porownania++;
        
        if (arr[i1] == pi1) 
           break; 
    }
    for(j1 = high; j1 >= low; j1--)
    {
        porownania++;
        if(arr[j1] == pi2)
                break;
    }
    
        
    int j = low + 1;  //zaczynamy powyzej low 
    int g = high - 1; //z drugiej strony zaczynamy ponizej high
    int k = low + 1;  
    swapy+=2;
    swap(&arr[low], &arr[i1]);
    swap(&arr[high], &arr[j1]);
    int p = arr[low]; //lewy pivot (kandydat) 
    int q = arr[high];  //kandydat na prawy pivot 
    
    while (k <= g)  
    {  
        // jezeli element jest mniejszy od lewego pivotu, 
        porownania+=2;
        if (arr[k] < p)
        {  
            porownania--;
            swapy++;
            swap(&arr[k], &arr[j]);  
            j++;  
        }  
        // if elements are greater than or equal  
        // to the right pivot  
        else if (arr[k] >= q)
        {  
            while (q < arr[g] && k < g)
            {
                g--;  
                porownania++;
            }
            swapy++;
            swap(&arr[k], &arr[g]);  
            g--;  
            porownania++;
            if (arr[k] < p)
            {  
                swapy++;
                swap(&arr[k], &arr[j]);  
                j++;  
            }  
        }  
        k++;  
    }  
    j--;  
    g++;  
  
    // ustawiamy pivoty.  
    swapy+=2;
    swap(&arr[low], &arr[j]);  
    swap(&arr[high], &arr[g]);  
  
    // lewy pivot ustawiamy jako j  
    *lp = j;   
  
    return g;   //prawy pivot to będzie g 
}

void dualquickSortSelect(int arr[], int low, int high)
{
  if (low < high)
  {
    int m = high-low+1;
    int pi1 = Select(arr,low, high, m/3);
    int pi2 = Select(arr, low, high, 2*m/3 );
    int lp;
    int rp = partition_d(arr, low, high, pi1,pi2, &lp); 
    dualquickSortSelect(arr, low, lp);
    dualquickSortSelect(arr, lp+1, rp);
    dualquickSortSelect(arr, rp+1, high);
  }
}

