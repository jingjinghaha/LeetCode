'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
# the O(n*k) definitely won't work
# even the following O(n*lgk) doesn't work
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq, sys
        if not nums or not k:
            return []
        heap = nums[0:k]
        heapq.heapify(heap)
        results = heapq.nlargest(1,heap)
        
        for i in range(k, len(nums)):
            heap[heap.index(nums[i-k])] = -sys.maxint
            heapq.heapify(heap)
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
            largest = heapq.nlargest(1, heap)
            results.extend(largest)
            
        return results

# the dynamic processing idea is keep a deque(), when shift right, remove the elements in the tail if it is smaller than the pending element. 
# as we also want to remmember the index of the elements in the deque when judging if an element exceed the window, so store the index of the element instend of the value. 
# with the index, we can quickly get out the value
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not nums or not k:
            return []
        q = deque()
        results = []
        for i in range(0, len(nums)):
            while len(q):
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)
            if q[0] < i - (k - 1):
                q.popleft()
            if i >= k-1:
                results.append(nums[q[0]])
            
        return results
