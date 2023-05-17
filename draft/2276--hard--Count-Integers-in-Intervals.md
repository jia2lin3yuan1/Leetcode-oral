#[2276. Count Integers in Intervals](https://leetcode.com/problems/count-integers-in-intervals/description/) 
+ `Hard`

Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

```
CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
```
Note that an interval [left, right] denotes all the integers x where left <= x <= right.



+ Example 1:

```
Input
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output
[null, null, null, 6, null, 8]

Explanation
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals.
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].
```

+ Constraints:

```
1 <= left <= right <= 109
At most 105 calls in total will be made to add and count.
At least one call will be made to count.
```

# Solution:
```python {.line-numbers}
def binaryInsertIndex_rht(st, end, val, listV):
    if st >= end:
        return st
    
    mid = (st + end) // 2
    # '<=', so comparing to right is '>', that right won't merge into the right intervals.
    if listV[mid] <= val:
        return binaryInsertIndex_rht(mid+1, end, val, listV)
    else:
        return binaryInsertIndex_rht(st, mid, val, listV)

def binaryInsertIndex_lft(st, end, val, listV):
    if st >= end:
        return st
    
    mid = (st + end) // 2
    if listV[mid] < val:  # '<', left won't merge to the left intervals
        return binaryInsertIndex_lft(mid+1, end, val, listV)
    else:
        return binaryInsertIndex_lft(st, mid, val, listV)
        

class CountIntervals:

    def __init__(self):
        self.intervals_lft = []
        self.intervals_rht = []
        self.count_int     = 0
        

    def add(self, left: int, right: int) -> None:
        N = len(self.intervals_lft)
        
        lft_idx = binaryInsertIndex_lft(0, N, left, self.intervals_rht)
        rht_idx = binaryInsertIndex_rht(0, N, right, self.intervals_lft)

        insert_idx = lft_idx
        new_lft = left if lft_idx == N else min(left, self.intervals_lft[lft_idx])
        new_rht = right if rht_idx == 0 else max(right, self.intervals_rht[rht_idx - 1])

        # pop removal intervals
        for _ in range(lft_idx, rht_idx):
            old_lft = self.intervals_lft.pop(lft_idx)
            old_rht = self.intervals_rht.pop(lft_idx)
            self.count_int -= (old_rht - old_lft + 1)
        
        # insert new intervals
        self.intervals_lft.insert(lft_idx, new_lft)
        self.intervals_rht.insert(lft_idx, new_rht)
        self.count_int += (new_rht - new_lft + 1)

    def count(self) -> int:
        return self.count_int


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
```

# Oral:
