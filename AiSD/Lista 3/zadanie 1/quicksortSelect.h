int findMedian(int arr[], int n) ///znajdz mediane danej czesci tablicy
    {
        sort(arr, arr+n);
        return arr[n/2];
    }
   
    void swap(int *a, int *b)
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
int partition_r(int arr[], int l, int r, int x) 
{ 
    int i; 
    for (i=l; i<r; i++)
    {
        porownania++;
        
        if (arr[i] == x) 
           break; 
    } 
    swapy++;
    swap(&arr[i], &arr[r]); 
  
    i = l; 
    for (int j = l; j <= r - 1; j++) 
    { 
        porownania++;
        if (arr[j] <= x) 
        { 
            swapy++;
            swap(&arr[i], &arr[j]); 
            i++; 
        } 
    }
    swapy++;
    swap(&arr[i], &arr[r]); 
    return i; 
} 
  
    int Select(int arr[], int l, int r, int k) 
{ 
    if (k > 0 && k <= r - l + 1) 
    { 
        int n = r-l+1; 
  
        int i, median[(n+4)/5]; 
        for (i=0; i<n/5; i++) 
            median[i] = findMedian(arr+l+i*5, 5); 
        porownania++;
        if (i*5 < n) 
        { 
            median[i] = findMedian(arr+l+i*5, n%5); 
            i++; 
        } 

        int medOfMed = (i == 1)? median[i-1]: Select(median, 0, i-1, i/2); 

        int pos = partition_r(arr, l, r, medOfMed); 
        porownania++;
        if (pos-l == k-1) 
            return arr[pos]; 
        porownania++;
        if (pos-l > k-1)  
            return Select(arr, l, pos-1, k); 
  
        return Select(arr, pos+1, r, k-pos+l-1); 
    } 
  
    return INT_MAX; 
} 


void quickSortSelect(int arr[], int low, int high)
{
  if (low < high)
  {
    int m = high-low+1;
    int pi = Select(arr,low, high, m/2);
     int p = partition_r(arr, low, high, pi); 
    quickSortSelect(arr, low, p - 1);
    quickSortSelect(arr, p + 1, high);
  }
}

