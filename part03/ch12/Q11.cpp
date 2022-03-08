#include <bits/stdc++.h>

using namespace std;

int n, k, l;
vector<pair<int, char>> dp;


int main() {
    int data[101][101] = {0};

    cin >> n;
    cin >> k;
    for (int i = 0; i < k; i++) {
        int a, b;
        cin >> a >> b;
        data[a][b] = 1;
    }
    cin >> l;
    for (int i = 0; i < l; i++) {
        int t;
        char c;
        cin >> t >> c;
        dp.push_back({t, c});
    }
    deque<pair<int, int>> snack;
    snack.push_back({1, 1});

    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};

    int snackIdx = 0;
    int dist = 0;
    int result = 0;
    int idx = 0;
    while (true) {
        int nx = snack.back().first + dx[dist];
        int ny = snack.back().second + dy[dist];
        result++;
        if (nx < 1 || ny < 1 || nx > n || ny > n) {
            cout << result << endl;
            return 0;
        }
        for (int i = 0; i < snack.size(); i++) {
            if (nx == snack[i].first && ny == snack[i].second) {
                cout << result << endl;
                return 0;
            }
        }
        if (data[nx][ny] == 1) {
            data[nx][ny] = 0;
        } else {
            snack.pop_front();
        }
        snack.push_back({nx, ny});
        if (idx < l) {
            if (result == dp[idx].first) {
                if (dp[idx].second == 'L') {
                    dist -= 1;
                    if (dist == -1) {
                        dist = 3;
                    }
                } else {
                    dist += 1;
                    if (dist == 4) {
                        dist = 0;
                    }
                }
                idx++;
            }
        }
    }
}
