#include<bits/stdc++.h>
#include <unistd.h>
using namespace std;

void process_mem_usage2(double& vm_usage, double& resident_set)
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
int getMax(vector<int> arr)
{
    int m = arr[0];
    for(int i = 1; i<arr.size(); i++)
    {
        m = arr[i] > m? arr[i] : m;
    }
    return m;
}

void countSort(vector<int> &arr, int exp)
{
    vector<int> output;
    output.resize(arr.size());
    int c[10] = {0};
    for(int i = 0; i<arr.size(); i++)
    {
        porownania++;
        c[(arr[i]/exp)%10]++;
    }
    for (int i = 1; i < 10; i++)
    {
        porownania++;
        c[i] += c[i - 1];
    }
    for(int i = arr.size()-1; i>=0; i--)
    {
        swapy++;
        output[c[(arr[i]/exp)%10]-1] = arr[i];
        c[(arr[i]/exp)%10]--;
    }
    arr = output;
}

void radixsort(vector<int> &arr, int cmp)
{
    swapy = 0;
    porownania = 0;
    int m = getMax(arr);

    for(int i = 1; m/i > 0; i*=10)
    {
        countSort(arr,i);
        
    }
    if(cmp==-1)
    {
        vector<int> out = arr;
        for(int i = 0; i <arr.size(); i++)
        {
            arr[i] = out[arr.size()-1-i];
        }
    }
}


