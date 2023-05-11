#[2100. Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/description/) 
+ `Medium`

You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.

The ith day is a good day to rob the bank if:
    - There are at least time days before and after the ith day,
    - The number of guards at the bank for the time days before i are non-increasing, and
    - The number of guards at the bank for the time days after i are non-decreasing.

More formally, this means day i is a good day to rob the bank if and only if 
```
security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].
```

Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in does not matter.



+ Example 1:

```
Input: security = [5,3,3,3,5,6,2], time = 2
Output: [2,3]
Explanation:
On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
```

+ Example 2:

```
Input: security = [1,1,1,1,1], time = 0
Output: [0,1,2,3,4]
Explanation:
Since time equals 0, every day is a good day to rob the bank, so return every day.
```

+ Example 3:

```
Input: security = [1,2,3,4,5,6], time = 2
Output: []
Explanation:
No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.
```


+ Constraints:

```
1 <= security.length <= 105
0 <= security[i], time <= 105
```

# Solution:
```python {.line-numbers}
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)

        dec_dist = [0] * length
        for k in range(1, length):
            if security[k] <= security[k - 1]:
                dec_dist[k] = dec_dist[k - 1] + 1

        inc_dist = [0] * length
        for k in range(length-2, -1, -1):
            if security[k] <= security[k + 1]:
                inc_dist[k] = inc_dist[k + 1] + 1

        days = [k for k in range(time, length-time) if inc_dist[k] >= time and dec_dist[k] >= time]
        return days

    def goodDaysToRobBank_stPointer(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        dec_dist = [0] * length
        inc_dist = [0] * length

        dec_st, inc_st = 0, 0
        for k, v in enumerate(security[1:]):
            pk, ck = k, k + 1

            dec_end = pk if v > security[pk] else (ck if ck == length - 1 else -1)
            if dec_end >= 0:
                for j in range(dec_st, dec_end + 1):
                    dec_dist[j] = j - dec_st # No. of days that are decreasing before j
                dec_st = ck

            inc_end = pk if v < security[pk] else (ck if ck == length - 1 else -1)
            if inc_end >= 0:
                for j in range(inc_st, inc_end + 1):
                    inc_dist[j] = inc_end - j # No. of days that are increasing after j
                inc_st = ck

        days = [k for k in range(length) if inc_dist[k] >= time and dec_dist[k] >= time]
        return days

```

# Oral:
