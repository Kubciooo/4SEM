#include <cstdio>
#include <cstdlib>
#include <ctime>
#include<bits/stdc++.h>
#define MAX_NUMBER 1000000
using namespace std;
int porownania = 0;
int swapy = 0;
void tworz_permutacje(vector<int>&A, int n)
{
    vector<bool> odw;
    odw.resize(n);
    A.resize(n);
    for(int i = 0; i<n; i++)
    {
        int k = rand()%n;
        while(odw[k])
            k = rand()%n;
        odw[k] = true;
        A[i] = k;
    }
}
void tworz_losowe(vector<int> &A, int n, int max_n)
{
    unordered_map<int,bool> M;
    A.resize(n);
    for(int i = 0; i<n; i++)
    {
        int k = rand()%max_n;
        while(M[k] == true)
            k = rand()%max_n;
        A[i] = rand()%max_n;
        M[k] = true;
    }
}

void wypisz(vector<int> A)
{
    for(int i = 0; i<A.size(); i++)
    {
        cout<<A[i]<<" ";
    }
    cout<<endl;
}

class Random_select
{
public:
    int partition(vector<int> &A, int p, int r)
    {
        int i = p + rand() % (r - p + 1); ///weź losową liczbę z przedziału od p do r
        swapy++;
        swap(A[r],A[i]);    ///chcemy, zeby A[i] bylo pivotem, wiec dajemy je na koniec
        int x = A[r];
        i = p - 1;
        for(int j=p; j<r; j++) ///idziemy od poczatku do koñca
        {
            porownania++;
            if(A[j] <= x)       ///jezeli A[j] <= pivot, A[j] ma byæ przed pivotem, czyli i++ -> jeden element wiêcej ma byæ przed pivotem
            {
                swapy++;
                i++;
                swap(A[i],A[j]);
            }
        }
        swapy++;
        swap(A[r],A[i+1]);
           cout<<"Uporzadkowana tablica: ";
           wypisz(A);
          cout<<"Pivot znajduje sie na miejscu "<<i+1<<endl<<endl;
        return i+1;
    }

    int recursiveSelect(vector<int>A, int p, int r, int i)
    {
          cout<<"aktualnie szukamy pivota w A["<<p<<"..."<<r<<"]\n";
        if(p == r)
            return A[p]; ///jezeli poczatek == koniec -> jestesmy na miejscu
        int q = partition(A, p, r);     /// q -> nasz pivot w tablicy A[p,..,r]
        int k = q - p + 1;               /// k to pozycja pivotu w naszej tablicy A[p,...,r], numerujemy od 1
        if(i == k)
            return A[q];          /// jezeli nasz pivot znajduje sie na pozycji i, to zwroc A[pivot]
        else if(i < k)
            return recursiveSelect(A, p, q-1, i);///jezeli pozyjca pivotu jest wieksza od i, to wiemy, ze elementy wieksze od A[q] nie sa tymi, ktore szukamy
        else
            return recursiveSelect(A, q+1, r, i-k);
    }

};

class Median_select
{
public:

    int findMedian(int arr[], int n) ///znajdz mediane danej czesci tablicy
    {
        sort(arr, arr+n);
        return arr[n/2];
    }
    int partition(int arr[], int l, int r, int x) ///znajdz miejsce pivota, x to pivot
    {
        int i;
        for (i=l; i<r; i++) ///przechodzimy po calej tablicy i szukamy x
        {
            porownania++;
            if(arr[i] == x)
                break;
        }
        swapy++;
        swap(&arr[i], &arr[r]);///dajemy pivot na koniec tablicy
        i = l;
        for (int j = l; j <= r - 1; j++)
        {
            porownania++;
            if (arr[j] <= x) ///elementy mniejsze od pivota dajemy na lewo od niego
            {
                swapy++;
                swap(&arr[i], &arr[j]);
                i++;
            }
        }
        swapy++;
        swap(&arr[i], &arr[r]);
          cout<<"Pivot znajduje sie na miejscu "<<i<<endl<<endl;
        return i;///no i zwracamy miejsce pivota
    }

    int Select(int arr[], int l, int r, int k)
    {
          cout<<"aktualnie szukamy pivota w A["<<l<<"..."<<r<<"]\n";

         cout<<"\nAktualnie szukamy liczby na pozycji "<<k<<endl;

        if (k > 0 && k <= r - l + 1) ///sprawdzamy, czy nie szukamy poza zakresem
        {
            int n = r-l+1; ///wielkosc tablicy
            int i, median[(n+4)/5]; ///dzielimy podtablice na tablice wielkosci 5, ostatnia podtablica moze miec wielkosc <=5
              cout<<"tablica median:\n";
            for (i=0; i<n/5; i++)
            {
                median[i] = findMedian(arr+l+i*5, 5);  ///liczymy mediany podtablic
                cout<<median[i]<<" ";
            }

            if (i*5 < n) ///ostatnia podtablica(jezeli istnieje)
            {
                median[i] = findMedian(arr+l+i*5, n%5);
                cout<<median[i]<<" ";
                i++;
            }
             cout<<endl;
             cout<<"Szukamy miediany median -> wejście do tablicy median\n";
            int medOfMed = (i == 1)? median[i-1]: Select(median, 0, i-1, i/2); ///jezeli mamy jedna mediane w tablicy - to mediana median to 1
            //cout<<"Miediana median to "<<medOfMed<<"\n";  ///inaczej schodzimy rekurencyjnie aby ja wyliczyc
            int pos = partition(arr, l, r, medOfMed); ///pozycja mediany median w tablicy
             cout<<"Mediana median jest na pozycji "<<pos<<endl;
            if (pos-l == k-1) ///traflismy w k-ty element
                return arr[pos];
            if (pos-l > k-1) ///jezeli jestesmy nad k-tym elementem, to chcemy zejsc nizej
                return Select(arr, l, pos-1, k);
            return Select(arr, pos+1, r, k-pos+l-1); ///jezeli jestesmy po k-tym elementem, to chcemy wejsc wyzej
        }
        return INT_MAX; ///wywalamy blad
    }

    void swap(int *a, int *b)
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }

};


double srednia(vector<int> v)
{
    int suma = 0;
    for(auto n : v)
    {
        suma += n;
    }
    return double(suma)/double(v.size());


}

double srednie_odchylenie(vector<int> v)
{
    int suma = 0;
    for(auto n : v)
    {
        suma += n;
    }
    double srednia = double(suma)/double(v.size());

    double odchylenie = 0;
    for(auto n : v)
    {
        odchylenie += (double(n)-srednia)*(double(n)-srednia);
    }
    odchylenie /= v.size();
    return sqrt(odchylenie);

}

void testuj(vector<int> arr, int n, int i, int liczba_testow)
{
    Random_select r1;
    Median_select s1;
    vector<int> porowania_random;
    vector<int> porownania_median;
    int arr2[n];
    int min_porownania_random, max_porownania_random = 0;
    int min_porownania_select, max_porownania_select = 0;
    for(int test_number = 0; test_number < liczba_testow; test_number++)
    {
        swapy = 0;
        porownania = 0;
        for(int i = 0; i<n; i++)
            arr2[i] = arr[i];
        int k = r1.recursiveSelect(arr,0,n-1, i);
        min_porownania_random = min(porownania, min_porownania_random);
        max_porownania_random = max(porownania, max_porownania_random);
        porowania_random.push_back(porownania);
        porownania = 0;
        swapy = 0;
        k = s1.Select(arr2,0,n-1,i);
        min_porownania_select = min(min_porownania_select, porownania);
        max_porownania_select = max(max_porownania_select, porownania);
        porownania_median.push_back(porownania);
    }
    cout<<"random - min: "<<min_porownania_random<<", max: "<<max_porownania_random<<", srednia: "<<srednia(porowania_random)<<", odchylenie: "<<srednie_odchylenie(porowania_random)<<endl;
    cout<<"select - min: "<<min_porownania_select<<", max: "<<max_porownania_select<<", srednia: "<<srednia(porownania_median)<<", odchylenie: "<<srednie_odchylenie(porownania_median)<<endl;
}
void wypisz(vector<int> arr, int n, int i)
{
    Random_select r1;
    Median_select s1;
    int arr2[n];
    bool flag = false;
    swapy = 0;
    porownania = 0;
    for(int i = 0; i<n; i++)
        arr2[i] = arr[i];

     cout<<"RANDOM SELECT:\n";
    int k = r1.recursiveSelect(arr,0,n-1, i);
    for(int j = 0; j<arr.size(); j++)
    {
        if(arr[j] == k && !flag)
        {
            cout<<"["<<arr[j]<<"] ";
            flag = true;
        }
        else
            cout<<arr[j]<<" ";
    }
    flag = false;
     cout<<"\nLiczba porownan: "<<porownania<<", Liczba swapow: "<<swapy;
    porownania = 0;
    swapy = 0;
     cout<<"\n\n\n\nSELECT:\n";
    k = s1.Select(arr2,0,n-1,i);
    for(int j = 0; j<sizeof(arr2)/sizeof(arr2[0]); j++)
    {
        if(arr[j] == k && !flag)
        {
            cout<<"["<<arr[j]<<"] ";
            flag = true;
        }
        else
            cout<<arr[j]<<" ";
    }

    cout<<"\nLiczba porownan: "<<porownania<<", Liczba swapow: "<<swapy<<endl;
    porownania = 0;
    swapy = 0;

}
int main(int argc, char* argv[])
{

    if(argc != 2)
    {
        cout<<"Niepoprawna liczba argumentów\n";
        return 1;
    }
    string type = argv[1];
    string t1 = "-p";
    string t2 = "-r";
    if(type != t1 && type != t2)
    {
        cout<<"Nieporawne dane wejściowe\n";
        return 0;
    }
    srand(time(NULL));
    vector<int> arr;
    cout<<"\nPodaj n\n";
    int n;
    cin>>n;
    int i;
    bool flag = false;
    cout<<"\nPodaj i\n";
    cin>>i;
    if(i > n)
    {
        cout<<"i > n!";
        return 1;
    }
    if(type == t2)tworz_losowe(arr,n,MAX_NUMBER);
    else tworz_permutacje(arr,n);
    for(auto i : arr)
    {
        cout<<i<<" ";
    }
    cout<<endl;
    wypisz(arr,n,i);
    //testuj(arr,n,i,10000);



    return 0;
}
