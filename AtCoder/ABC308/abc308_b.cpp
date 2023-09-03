#include <iostream>
using namespace std;

int main () {
    int n,m;
    cin >> n >> m;

    string c[n], d[m];
    int p[m+1];

    for (int i=0; i < n; i++) {
        cin >> c[i];
    }

    for (int i=0; i < m; i++) {
        cin >> d[i];
    }

    for (int i=0; i < m+1; i++) {
        cin >> p[i];
    }

    int total = 0;

    for (int i=0; i < n; i++) {
        int price = p[0];
        for(int j=0; j < m; j++) {
            if (c[i] == d[j]) {
                price = p[j+1];
            }
        }

        total += price;
    }
    
    cout << total;

    return 0;
}