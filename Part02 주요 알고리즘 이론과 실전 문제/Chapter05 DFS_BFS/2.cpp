#include <bits/stdc++.h>

using namespace std;

int n, m;
int data[200][200];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &data[i][j]);
        }
    }

    queue<pair<int, int>> q;
    q.push({0, 0});
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                continue;
            }
            if (data[nx][ny] == 1) {
                data[nx][ny] = data[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    cout << data[n - 1][m - 1] << '\n';
}
