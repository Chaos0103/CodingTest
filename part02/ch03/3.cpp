#include <bits/stdc++.h>

using namespace std;

int n, m;
int result = 0;

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int min_value = 10001;
        for (int j = 0; j < m; j++) {
            int num;
            cin >> num;
            min_value = min(min_value, num);
        }
        result = max(result, min_value);
    }

    cout << result;
}