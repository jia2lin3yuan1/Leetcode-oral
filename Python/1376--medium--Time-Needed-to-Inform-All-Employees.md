#[1376. Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/description/) 
+ `Medium`
+ open the link for visualization example

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.


+ Example 1:
```
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
```

+ Example 2:
```
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
```

+ Constraints:
```
1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
```

# Solution:
```python {.line-numbers}
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:  
        # convert the manager list to subordinates dictionary
        # so that given i, we can easily check all its subordinates
        subordinates = dict()
        for k, m in enumerate(manager):
            if m not in subordinates:
                subordinates[m] = []
            subordinates[m].append(k)

        # BFS traverse
        max_time = 0
        stack = [(headID, 0)]
        while len(stack) > 0:
            node, time = stack.pop(0)

            if node not in subordinates:
                max_time = max(max_time, time)
            else:
                stack.extend([(k, time + informTime[node]) for k in subordinates[node]])
    
        return max_time
```

# Oral:
Since the subordination relationships have a tree structure, our first step is to convert the manager list into a tree-like structure representing the subordinates. Afterwards, we employ the BFS algorithm to traverse the tree, starting from the headID. During the traversal, we keep track of each employee's ID and the time it takes for them to receive the message.

Thus, after the traversal, the max-time over all nodes is the number of minutes it needs to inform all employees.

Time complexity: O(N)

space complexity: O(N)
