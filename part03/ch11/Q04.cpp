#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> coins;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        coins.push_back(x);
    }

    sort(coins.begin(), coins.end());

    int result = 1;
    for (int i = 0; i < n; i++) {
        if (result < coins[i]) {
            break;
        }
        result += coins[i];
    }

    cout << result << endl;
}
