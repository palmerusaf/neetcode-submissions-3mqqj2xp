class Solution {
  /**
   * @param {number} n
   * @param {number[][]} edges
   * @returns {boolean}
   */
  validTree(n, edges) {
    if (!edges.length) return true;
    const adj = {};
    const vis = new Set();
    for (const [n1, n2] of edges) {
      adj[n1] ? adj[n1].push(n2) : (adj[n1] = [n2]);
      adj[n2] ? adj[n2].push(n1) : (adj[n2] = [n1]);
    }

    return dfs(0, -1) && vis.size == n;

    function dfs(i, prev) {
      if (vis.has(i)) return false;
      vis.add(i);
      for (const j of adj[i]) {
        if (prev === j) continue;
        if (!dfs(j, i)) return false;
      }
      return true;
    }
  }
}

