#[785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/description/) 
+ `Medium`
+ open the link to view visualization example

There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

```
- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected).
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
```

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

+ Example 1:
```
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
```

+ Example 2:

```
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
```

+ Constraints:

```
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
```

# Solution:
```python {.line-numbers}
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        visited = dict()

        for k in range(N):
            if k in visited:
                continue

            # take k as the source node, iterative over the sub-graph including k
            visited[k] = 1
            stack = [k]
            while len(stack) > 0:
                top = stack.pop()
                for j in graph[top]:
                    # if j not visited, assign it a party different from k.
                    if j not in visited:
                        visited[j] = 0 if visited[top] else 1
                        stack.append(j)

                    # if the party of j is same as the party of k, the graph is not Bipartite.
                    if visited[j] == visited[top]:
                        return False

        return True
```

# Oral:
To check if a graph is bipartite, we perform DFS iteration over the graph. Since the graph may consist of multiple that are not directly connected, we employ a for-loop to process each node individually. Regarding a node `k`, if it is not visited yet, we run the DFS algorithm to check if the corresponding subgraph is bipartite. If not, return `False`.

If all possible subgraphs are bipartite, the graph is bipartite and we return `True`

Time complexity: O(N)

space complexity: O(N)
