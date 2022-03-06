#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> food_times, long long k) {

    long long sum = 0;
    for (int i = 0; i < food_times.size(); i++) {
        sum += food_times[i];
    }
    if (sum <= k) return -1;

    priority_queue<pair<int, int>> pq;
    for (int i = 0; i < food_times.size(); i++) {
        pq.push({-food_times[i], i + 1});
    }
    long long previous = 0;
    long long sum_time = 0;
    long long length = food_times.size();
    while (sum_time + ((-pq.top().first - previous)* length) <= k) {
        int now = -pq.top().first;
        pq.pop();
        sum_time += (now - previous) * length;
        previous = now;
        length--;
    }

    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    sort(result.begin(), result.end());
    return result[(k - sum_time) % length];
}

vector<int> food_times = {3, 1, 2};
int k = 5;

int main() {
    cout << solution(food_times, k) << endl;
}
