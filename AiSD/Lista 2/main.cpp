#include<bits/stdc++.h>
#include <stdio.h>
#include <chrono>
#include <random>
#include "compare.h"
#include "quicksort.h"
#include "mergesort.h"
#include "insertsort.h"
#include "dualPivot.h"
#include "insert-merge.h"
using namespace std;
int cmp = 0;



void randomize(vector<int> &V, int from, int to, int size)
{
    random_device r;
    default_random_engine e1(r());
    uniform_int_distribution<int> uniform_dist(from, to);
    int mean = uniform_dist(e1);
        V.resize(size);
        for(int i = 0; i<size; i++)
        {
                int mean = uniform_dist(e1);
                V[i] = mean;
        }
}
void printVector(vector<int> V)
{
        for(int i = 0; i<V.size(); i++)
        {
                printf("%d ",V[i]);
        }
        printf("\n");

}


int main(int argc, char *argv[])
{

  if(argc != 5 && argc != 8 && argc != 9) return 1;
  string type = argv[2];
  string comp = argv[4];
  if(comp == ">=")cmp = -1;
  else cmp = 1;

  chrono::steady_clock sc;

  vector<int> data;


  if(argc==8)
  {
         string s = argv[7];
         int k = stoi(s);
         char* f = argv[6];
         fstream file;
         file.open(f, ios::out);
         //file << "typj sortdowania: " + type + "\n";
         for(int n = 100; n <= 10000; n += 100)
         {
                data.clear();
                data.resize(n);
                for(int i = 0; i<k; i++)
                {
                         randomize(data, 0, 2*n, n);
                         porownania = 0;
                         swapy = 0;
                         auto start = sc.now();     // start timer
                         if(type=="quick")quickSort(data, 0, n - 1,cmp);
                         if(type=="merge")mergesort(data,0,n-1,cmp);
                         if(type=="insert")insertSort(data,cmp);
                         if(type=="dualquick")DualPivotQuickSort(data,0,n-1,cmp);
                         if(type=="insert-merge")
                         {
                                int data2[n];
                                for(int i = 0; i<n; i++)
                                        data2[i] = data[i];
                                start = sc.now();
                                mergesort2(4,data2,0,n-1,"<=");

                         }
                         auto end = sc.now();
                         auto time_span = static_cast<chrono::duration<double>>(end - start);
                         string time_taken = to_string(static_cast<chrono::duration<double>>(end - start).count());
                         file <<"n: "<<n<<", czas: "<<time_taken<<", swapy: "<<swapy<<", porównania: "<<porownania<<"\n";
                }
         }

        file.close();
    }
    else if(argc==5)
    {
         int n;
         cin>>n;
         data.resize(n);
         for(int i = 0; i<n; i++)
                cin>>data[i];
         porownania = 0;
         swapy = 0;
         auto start = sc.now();     // start timer
         if(type=="quick")quickSort(data, 0, n - 1,cmp);
         if(type=="merge")mergesort(data,0,n-1,cmp);
         if(type=="insert")insertSort(data,cmp);
         if(type=="dualquick")DualPivotQuickSort(data,0,n-1,cmp);

         auto end = sc.now();
         auto time_span = static_cast<chrono::duration<double>>(end - start);
         printf("%.10f sekund\nporownania: %d, swapy: %d\n", time_span, porownania,swapy);
         printVector(data);

    }
    else if(argc==9)
    {
         string temp = argv[6];
         char* filename = argv[8];
         int MAX = stoi(temp);
         if(type=="insert-merge")
         {

                string datatype = argv[4];

                if(datatype == "string")
                {

                        string data[1001];
                        int n;
                        cin>>n;
                        for(int i = 0; i<n; i++)
                        {
                                cin>>data[i];
                        }
                        auto start = sc.now();     // start timer
                        mergesort2<string>(MAX,data,0,n-1,filename);
                        auto end = sc.now();
                         auto time_span = static_cast<chrono::duration<double>>(end - start);
                        printf("%.10f sekund\nporownania: %d, swapy: %d\n", time_span, porownania,swapy);
                        for(int i = 0; i<n; i++)
                                cout<<data[i]<<" ";
                        cout<<endl;
                }
                else if(datatype == "int")
                {
                        int data[10001];
                        int n;
                        cin>>n;
                        for(int i = 0; i<n; i++)
                        {
                                cin>>data[i];
                        }
                        auto start = sc.now();     // start timer
                        mergesort2<int>(MAX,data,0,n-1,filename);
                        auto end = sc.now();
                         auto time_span = static_cast<chrono::duration<double>>(end - start);
                        printf("%.10f sekund\nporownania: %d, swapy: %d\n", time_span, porownania,swapy);
                        for(int i = 0; i<n; i++)
                                cout<<data[i]<<" ";
                        cout<<endl;
                }
                  else if(datatype == "float")
                {
                        float data[10001];
                        int n;
                        cin>>n;
                        for(int i = 0; i<n; i++)
                        {
                                cin>>data[i];
                        }
                        auto start = sc.now();     // start timer
                        mergesort2<float>(MAX,data,0,n-1,filename);
                        auto end = sc.now();
                         auto time_span = static_cast<chrono::duration<double>>(end - start);
                        printf("%.10f sekund\nporownania: %d, swapy: %d\n", time_span, porownania,swapy);
                        for(int i = 0; i<n; i++)
                                cout<<data[i]<<" ";
                        cout<<endl;
                }

         }

    }

    return 0;
}




