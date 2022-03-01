#include <bits/stdc++.h>

using namespace std;

int n, k;
vector<int> a;
vector<int> b;

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        a.push_back(num);
    }
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        b.push_back(num);
    }
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for (int i = 0; i < k; i++) {
        if (a[i] < b[n - 1 - i]) {
            swap(a[i], b[n - 1 - i]);
        } else break;
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
        result += a[i];
    }
    cout << result << endl;
}