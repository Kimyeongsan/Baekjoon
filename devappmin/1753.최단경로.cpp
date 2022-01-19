/**
 * @file 1753.최단경로.cpp
 * @author @devappmin
 * @brief 최단경로 (골드5)
 * @version 0.1
 * @date 2022-01-19
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 * 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
 *
 * 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다.
 * (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
 * 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
 * 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다.
 * 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
 *
 * 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다.
 * 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 20001
#define INF 1000000000

using namespace std;

vector<pair<int, int> > vt[MAX];
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;
int dist[MAX];

void solution(int v, int e, int s) {
    while (!pq.empty()) {
        int d, i;
        tie(d, i) = pq.top();
        pq.pop();

        if (d > dist[i])
            continue;
        else {
            for (int idx = 0; idx < vt[i].size(); idx++) {
                if (dist[vt[i][idx].first] > d + vt[i][idx].second) {
                    dist[vt[i][idx].first] = d + vt[i][idx].second;
                    pq.push(pair<int, int>(dist[vt[i][idx].first], vt[i][idx].first));
                }
            }
        }
    }

    for (int i = 1; i <= v; i++) {
        if (dist[i] == INF)
            cout << "INF\n";
        else
            cout << dist[i] << "\n";
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int v, e, s, a, b, c;
    cin >> v >> e >> s;

    for (int i = 0; i < e; i++) {
        cin >> a >> b >> c;
        vt[a].push_back(pair<int, int>(b, c));
    }

    for (int i = 1; i <= v; i++) {
        if (i == s) {
            pq.push(pair<int, int>(0, i));
            dist[i] = 0;
        } else {
            pq.push(pair<int, int>(INF, i));
            dist[i] = INF;
        }
    }

    solution(v, e, s);

    return 0;
}