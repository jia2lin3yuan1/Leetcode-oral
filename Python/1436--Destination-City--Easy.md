#[1436. Destination City](https://leetcode.com/problems/destination-city/description/) 
+ `Easy`

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.


+ Example 1:

```
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
```

+ Example 2:

```
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
```

+ Example 3:

```
Input: paths = [["A","Z"]]
Output: "Z"
```


+ Constraints:

```
1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
```

# Solution:
```python {.line-numbers}
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out_cities = set()
        for ele in paths:
            out_cities.add(ele[0])

        for ele in paths:
            if ele[1] not in out_cities:
                return ele[1]
```

# Oral:
We can solve the problem with the data structure set(), so that look-up time is O(1).

We first go through each path in paths, store all outgoing cities in the set()

Then, we go through each path in paths again, for each ingoing city, if it is not in the outgoing set, it is the destination.


The time complexity is: O(N).

The spatial complexity is: O(N)
