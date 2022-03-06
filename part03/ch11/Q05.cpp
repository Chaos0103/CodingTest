#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> data;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        data.push_back(x);
    }

    int result = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (data[i] != data[j]) {
                result++;
            }
        }
    }

    cout << result << endl;
}
