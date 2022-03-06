#include <bits/stdc++.h>

using namespace std;

int n, result;
vector<int> data;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        data.push_back(x);
    }

    sort(data.begin(), data.end());

    int cnt = 0;
    for (int i = 0; i < data.size(); i++) {
        cnt++;
        if (cnt >= data[i]) {
            result++;
            cnt = 0;
        }
    }

    cout << result << endl;
}
