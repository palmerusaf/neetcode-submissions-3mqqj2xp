class Solution {
  /**
   * @param {number} n
   * @param {number[][]} edges
   * @returns {number}
   */
  countComponents(n, edges) {
    if (!edges.length) return n;
    const vis = {};
    let count = 0;
    const mp = {};
    for (const [n1, n2] of edges) {
      mp[n1] ? mp[n1].push(n2) : (mp[n1] = [n2]);
    }
    for (const [n2, n1] of edges) {
      mp[n1] ? mp[n1].push(n2) : (mp[n1] = [n2]);
    }
    for (const n in mp) {
      if (!vis[n]) count++;
      dfs(n, n);
    }
    function dfs(n, prevN) {
      if (vis[n]) return;
      vis[n] = true;
      for (const ad of mp[n]) {
        if (ad === prevN) continue;
        dfs(ad, n);
      }
    }
    return count;
  }
}

