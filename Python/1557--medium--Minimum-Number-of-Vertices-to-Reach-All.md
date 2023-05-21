#[1557. Minimum Number of Vertices to Reach All](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/) 
+ `Medium`

Given a `directed acyclic graph`, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.


+ Example 1:

```
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
```


+ Example 2:

```
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.
```


+ Constraints:

```
2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
```

# Solution:
```python {.line-numbers}
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes_lut = dict()
        for ele in edges:
            nodes_lut[ele[1]] = 0

        ans = [k for k in range(n) if k not in nodes_lut]
        return ans
```

# Oral:
In a directed acyclic graph, if a node `k` can be reached by another node, which means there exists an edge with `edge[1] = k`, then the node cannot be in the desired set. Instead, the node that has no incoming edges and can reach node `k` should be in the set.

Thus, what we need to do is iterate over the edges and find the nodes that never appear in the `to` location of any edges.
