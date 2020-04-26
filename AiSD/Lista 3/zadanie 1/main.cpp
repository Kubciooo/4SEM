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
#include "radix.h"
#include "quicksortSelect.h"
#include <iostream>
#include <fstream>
#include <unistd.h>
#include "dualpivotselect.h"
using namespace std;
int cmp = 0;


void process_mem_usage(double& vm_usage, double& resident_set)
{
    vm_usage     = 0.0;
    resident_set = 0.0;

    // the two fields we want
    unsigned long vsize;
    long rss;
    {
        std::string ignore;
        std::ifstream ifs("/proc/self/stat", std::ios_base::in);
        ifs >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore
                >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore >> ignore
                >> ignore >> ignore >> vsize >> rss;
    }

    long page_size_kb = sysconf(_SC_PAGE_SIZE) / 1024; // in case x86-64 is configured to use 2MB pages
    vm_usage = vsize / 1024.0;
    resident_set = rss * page_size_kb;
}
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
         for(int n = 10; n <= 100000; n +=100)
         {
                data.clear();
                data.resize(n);
                for(int i = 0; i<k; i++)
                {
                         randomize(data, 0, 10*n, n);
                         porownania = 0;
                         swapy = 0;
                         auto start = sc.now();     // start timer
                         if(type=="quick")quickSort(data, 0, n - 1,cmp);
                         if(type=="merge")mergesort(data,0,n-1,cmp);
                         if(type=="radix")radixsort(data,cmp);
                         if(type=="insert")insertSort(data,cmp);
                         if(type=="dualquick")DualPivotQuickSort(data,0,n-1,cmp);
                         if(type == "quickselect")
                         {
                                int data2[n];
                                for(int i = 0; i<n; i++)
                                        data2[i] = data[i];
                                start = sc.now();
                                quickSortSelect(data2, 0, n-1);
                         }
                         if(type == "dualselect")
                         {

                                int data2[n];
                                for(int i = 0; i<n; i++)
                                  data2[i] = data[i];
                                 start = sc.now();
                                  dualquickSortSelect(data2, 0, n-1);
                                 for(int i = 0; i < n; i++)
                                {      
                                         data[i] = data2[i];
                                }
         
                        }
                         if(type=="insert-merge")
                         {
                                int data2[n];
                                for(int i = 0; i<n; i++)
                                        data2[i] = data[i];
                                start = sc.now();
                                mergesort2(4,data2,0,n-1,"<=");

                         }
                         double vm_usage, resident_set;
                         process_mem_usage(vm_usage, resident_set); 
                         auto end = sc.now();
                         auto time_span = static_cast<chrono::duration<double>>(end - start);
                         string time_taken = to_string(static_cast<chrono::duration<double>>(end - start).count());
                         file <<" "<<n<<" "<<time_taken<<" "<<swapy<<" "<<porownania<<" "<<resident_set<<"\n";
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
         if(type=="radix")radixsort(data,cmp);
         if(type == "quickselect")
         {

                  int data2[n];
                  for(int i = 0; i<n; i++)
                       data2[i] = data[i];
                  start = sc.now();
                  quickSortSelect(data2, 0, n-1);
                  for(int i = 0; i < n; i++)
                  {
                        data[i] = data2[i];
                  }
         }
         if(type == "dualselect")
         {
                int data2[n];
                  for(int i = 0; i<n; i++)
                       data2[i] = data[i];
                  start = sc.now();
                  dualquickSortSelect(data2, 0, n-1);
                  for(int i = 0; i < n; i++)
                  {
                        data[i] = data2[i];
                  }
         
         }
         
         auto end = sc.now();
         double vm_usage, resident_set;
         process_mem_usage(vm_usage, resident_set); 
         auto time_span = static_cast<chrono::duration<double>>(end - start);
         printf("%.10f sekund\nporownania: %d, swapy: %d\n", time_span, porownania,swapy);
         printf("%.10fkB memory, %.10fkb resident_set\n", vm_usage , resident_set);
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




