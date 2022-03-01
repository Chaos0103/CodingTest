#include <bits/stdc++.h>

using namespace std;

int n, m, k;

int main() {

    int array[1000];

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        cin >> array[i];
    }

    sort(array, array + n);

    int first = array[n - 1];
    int second = array[n - 2];
    int result = (m / (k + 1) * k + m % (k + 1)) * first;
    result += m / (k + 1) * second;

    cout << result;
}