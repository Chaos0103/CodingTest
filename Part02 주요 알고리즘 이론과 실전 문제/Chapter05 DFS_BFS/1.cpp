#include <bits/stdc++.h>

using namespace std;

int n, m;
int data[1000][1000];

bool dfs(int x, int y) {
    if (x < 0 || y < 0 || x >= n || y >= m) {
        return false;
    }
    if (data[x][y] == 0) {
        data[x][y] = 1;
        dfs(x + 1, y);
        dfs(x - 1, y);
        dfs(x, y + 1);
        dfs(x, y - 1);
        return true;
    }
    return false;
}


int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &data[i][j]);
        }
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dfs(i, j)) {
                result += 1;
            }
        }
    }

    cout << result << '\n';
}
