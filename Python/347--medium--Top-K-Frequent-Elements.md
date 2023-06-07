#[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/) 
+ `Medium`

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


+ Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

+ Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```


+ Constraints:

```
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
```


# Solution:
```python {.line-numbers}
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # iterative over nums to count frequences
        lut = dict()
        for v in nums:
            lut[v] = 1 if v not in lut else lut[v] + 1

        # traverse the look-up-table, and maintain a top_k stack to find topk frequent elements
        # Perform binaryInsert when need to insert an element, to get O(nlogn) time complexity.
        top_k = []
        for v, f in lut.items():
            if len(top_k) == k and f < top_k[-1][1]:
                continue
            elif len(top_k) == k:
                top_k.pop(-1)

            self.binaryInsert(v, f, 0, len(top_k), top_k)
        
        return [ele[0] for ele in top_k]
    
    def binaryInsert(self, val, frq, st, end, decList):
        if st >= end:
            decList.insert(st, (val, frq))
            return
        
        mid = (st + end) // 2
        if decList[mid][1] > frq:
            self.binaryInsert(val, frq, mid+1, end, decList)
        else:
            self.binaryInsert(val, frq, st, mid, decList)
```

# Oral:
To solve a frequence problem, we can begin by iterating over the input list to compute frequences and saved in a lookup table.

Afterwards, we traverse the lookup table and maintain a topK stack to identify the top K frequent elements. When a new item in the lookup table need to be added to the topK stack, we utilize the binaryInsert algorithm to enhance time efficiency.

+ Time complexity: O(Nlog(N))
+ Space complexity: O(N)


