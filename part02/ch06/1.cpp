#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> data;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        data.push_back(num);
    }
    sort(data.begin(), data.end());

    for (int i = n - 1; i >= 0; i--) {
        cout << data[i] << ' ';
    }
}
