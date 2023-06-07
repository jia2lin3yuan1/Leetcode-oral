#[282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/description/) 
+ `Hard`

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

+ Example 1:
```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
```

+ Example 2:

```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
```

+ Example 3:

```
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
```
+ Constraints:

```
1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1
```

# Solution:
```python {.line-numbers}
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        #  return self.addOperators_bruteforce(num, target)
        out_expressions = []
        self.dfsMath(num, target, out_expressions,
                    pos = 1,
                    path = num[0],
                    sumV = int(num[0]),
                    lastV = int(num[0]),
                    path_lastV = num[0],
                    path_lastOp = '+' )
        return out_expressions

    def dfsMath(self, num, target, out_expressions,
                      pos=0, path='',
                      sumV=0, lastV=0,
                      path_lastV='',
                      path_lastOp = '+'):
        '''
        DFS search with some basic mathmatic analysis. There are 4 possible way to extend the path when it meets a new position 'pos': +, -, *, longer variable.

        Converting -/* to + with below formulations:
        # 'sum - v' ==> sum + (-v)
        # 'sum0 + last * v' ==> sum1 - last + (last * v),
            where sum1 = sum0 + last, it has been updated in the last step.

        And for longer variable, it need to consider what is the last-operation to decide the moving on strategy.
        '''
        # if position meets the end and sumV meets the target,
        if pos == len(num):
            if sumV == target:
                out_expressions.append(path)
            return

        # try 3 possible operations, [+, -, *]
        curV = int(num[pos])
        self.dfsMath(num, target, out_expressions,
                     pos = pos + 1,
                     path = path + '+' + num[pos],
                     sumV = sumV + curV,
                     lastV = curV,
                     path_lastV = num[pos],
                     path_lastOp = '+' )
        self.dfsMath(num, target, out_expressions,
                     pos = pos + 1,
                     path = path + '-' + num[pos],
                     sumV = sumV - curV,
                     lastV = -curV,
                     path_lastV = num[pos],
                     path_lastOp = '-'
                     )
        curV = lastV * int(num[pos])
        self.dfsMath(num, target, out_expressions,
                     pos = pos + 1,
                     path = path + '*' + num[pos],
                     sumV = sumV - lastV + curV,
                     lastV = curV,
                     path_lastV = num[pos],
                     path_lastOp = '*'
                     )

        # if the last variable in path is starting with '0',
        # the num[0] can be directly addict to it and becomes a longer variabale
        if int(path_lastV) > 0:
            curV = int(path_lastV + num[pos])
            if path_lastOp == '*':
                curV = lastV / int(path_lastV) * curV
            else:
                curV = curV if path_lastOp == '+' else -1 * curV

            self.dfsMath(num, target, out_expressions,
                        pos = pos + 1,
                        path = path + num[pos],
                        sumV = sumV - lastV + curV,
                        lastV = curV,
                        path_lastV = path_lastV + num[pos],
                        path_lastOp = path_lastOp
                        )


    def addOperators_bruteforce(self, num, target):
        expressions = [(num[0], num[0])]
        for v in num[1:]:
            num_exp = len(expressions)
            for i in range(num_exp):
                topExp, topV = expressions.pop(0)
                expressions.extend([(topExp + '+' + v, v),
                                    (topExp + '-' + v, v),
                                    (topExp + '*' + v, v) ])
                if int(topV) > 0:
                    expressions.append((topExp + v, topV+v))

        ans = []
        for exp, _ in expressions:
            if self.computeExpression(exp) == target:
                ans.append(exp)

        return ans

    def computeExpression(self, expression):
        operations = {'+': lambda x, y: x + y,
                      '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y,
                      }

        values, ops = [], []
        s = ''
        for ele in expression:
            if ele not in ['+', '-', '*']:
                s += ele
                continue

            # process * first
            if len(ops) > 0 and ops[-1] == '*':
                values.append(operations[ops.pop()](values.pop(), int(s)))
            else:
                values.append(int(s))
            ops.append(ele)
            s = ''

        if len(ops) > 0 and ops[-1] == '*':
            values.append(operations[ops.pop()](values.pop(), int(s)))
        else:
            values.append(int(s))

        # process +/-
        rst = values[0]
        for op, val in zip(ops, values[1:]):
            rst = operations[op](rst, val)

        return rst

```

# Oral:
