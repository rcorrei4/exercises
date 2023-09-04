#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main () {
    int n;
    int l;

    cin >> n >> l;

    vector<string> v;
    for(int i=0; i < n; i++){
        string x;
        cin >> x;
        v.push_back(x);
    }

  
    sort(v.begin(), v.end());
  
    string out = "";
    for (auto x : v)
        out += x;
    
    cout << out;
    return 0;
}