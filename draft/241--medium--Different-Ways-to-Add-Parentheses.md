#[241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/) 
+ `Medium`
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.


+ Example 1:
```
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
```

+ Example 2:
```
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```
 
+ Constraints:
```
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
```

# Solution:
```python {.line-numbers}
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # parse the expression into elements and operations
        operations = ['+', '-', '*']
        cur, elements, ops = '', [], []
        for k in range(len(expression)-1, -1, -1):
            if expression[k] in operations:
                ops.insert(0, expression[k])
                elements.insert(0, int(cur))
                cur = ''
            else:
                cur = expression[k] + cur
        elements.insert(0, int(cur))

        # find different ways to add parentheses
        visited = dict()
        return self.diffWaysToCompute_dp(elements, visited, ops)

    def diffWaysToCompute_dp(self, elements, visited, ops):
        operations = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y
                }

        key = '()'.join([str(v) for v in elements]) + ' || ' + ''.join(ops)
        if key in visited:
            return visited[key]

        if len(elements) == 1:
            # single integer
            return [elements[0]]
        elif len(elements) == 2:
            # single operator
            visited[key] = [operations[ops[0]](elements[0], elements[1])]
            return visited[key]

        # iterate operators for which one should be computed at last
        visited[key] = []
        for k, op in enumerate(ops):
            lft = self.diffWaysToCompute_dp(elements[:k+1], visited, ops[:k])
            rht = self.diffWaysToCompute_dp(elements[k+1:], visited, ops[k+1:])
            for lv in lft:
                for rv in rht:
                    visited[key].append(operations[op](lv, rv))

        return visited[key]

```

# Oral:
