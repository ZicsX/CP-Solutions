#include<bits/stdc++.h>
#include<fstream>
#include<iostream>
#include<random>
#include<chrono>

#define int long long
using namespace std;

struct custom_hash {
  static int splitmix64(int x) {
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    return x;
  }
  size_t operator()(int x) const {
    static
    const int FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
    return splitmix64(x + FIXED_RANDOM);
  }
};
int MergeEdge(int u, int v) {
  if (u > v) swap(u, v);
  return u * 200001 + v;
}
pair < int, int > SplitEdge(int w) {
  return {
    w / 200001,
    w % 200001
  };
}
int n, m, q, s[200001];
vector < pair < int, int >> a[200001];

signed main() {

  ifstream in ; in .open("in.txt");
  ofstream out;
  out.open("out.txt");

  int T; in >> T;
  for (int i = 1; i <= T; ++i) {
    out << "Case #" << i << ": ";

    in >> n >> m >> q;
    for (int i = 1; i <= n; ++i) {
      s[i] = 0;
      a[i].clear();
    }
    unordered_map < int, int, custom_hash > G, F;
    vector < int > c;
    map < int, int > Q;
    for (int i = 1; i <= m; ++i) {
      int u, v, w; in >> u >> v >> w;
      Q[MergeEdge(u, v)] += w;
    }
    for (pair < int, int > i: Q) {
      int u, v, w;
      auto t = SplitEdge(i.first);
      u = t.first;
      v = t.second;
      w = i.second;
      if (u < 1 || u > n || v < 1 || v > n) continue;
      a[u].push_back({
        v,
        w
      });
      a[v].push_back({
        u,
        w
      });
      G[MergeEdge(u, v)] += w;
      s[u]++;
      s[v]++;
    }
    for (int i = 1; i <= n; ++i)
      if (s[i] >= 400)
        c.push_back(i);
      else {
        for (int j = 0; j < (int) a[i].size(); ++j)
          for (int k = j + 1; k < (int) a[i].size(); ++k)
            F[MergeEdge(a[i][j].first, a[i][k].first)] +=
            min(a[i][j].second, a[i][k].second);
      }
    for (int i = 1; i <= q; ++i) {
      int u, v, s = 0; in >> u >> v;
      for (int j: c)
        s += min(G[MergeEdge(u, j)], G[MergeEdge(j, v)]);
      out << s + F[MergeEdge(u, v)] + 2 * G[MergeEdge(u, v)] << ' ';
    }
    out << endl;
  }
}
