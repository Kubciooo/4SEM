#include<bits/stdc++.h>

using namespace std;


void tworz_tablice(vector<int> &v, int n)
{
    v.clear();
    for(int i = 1; i<n; i++)
        v.push_back(2*i);
}


int binSearch(vector<int> V, int p, int k, int x, int porownania, int poziom)
{
    porownania++;
    if(p >= k)
    {
        ///cout<<"T("<<poziom<<") = "<<porownania<<"\n";
        if(V[p] == x)
            return 1;
        return 0;
    }
    int sr = (p+k)/2;
    porownania+=2;
    if(V[sr] == x)
    {
        porownania--;
       /// cout<<"T("<<poziom<<") = "<<porownania<<"\n";
        return 1;
    }
    else if(V[sr] > x)
    {
        return binSearch(V, p, sr-1, x, porownania, poziom+1);
    }
    else
    {
        return binSearch(V,sr+1,k,x,porownania,poziom+1);

    }
}


int main()
{
    vector<int> V;
    srand(time(NULL));
    int n;
    cout<<"Podaj n: ";
    cin>>n;
    V.resize(n);
    cout<<"Podaj posortowana tablice: ";
    for(int i = 0; i<n; i++)
    {
        cin>>V[i];
    }
    cout<<"Podaj szukana liczbe: ";
    int k;
    cin>>k;
    cout<<binSearch(V,0,V.size()-1, k, 0, 0);


    return 0;
}
