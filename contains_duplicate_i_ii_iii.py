'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        val_set = set()
        for val in nums:
            if val in val_set:
                return True
            val_set.add(val)
        return False


'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_map = {}
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = [i]
            else:
                for idx in index_map[nums[i]]:
                    if abs(idx - i) <= k:
                        return True
                index_map[nums[i]].append(i)
        return False


'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
'''
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        import bisect
        sorted_nums = []
        index_map = {}
        for i in range(len(nums)):
            pos1 = bisect.bisect_left(sorted_nums, nums[i] - t)
            pos2 = bisect.bisect_right(sorted_nums, nums[i] + t)
            for j in range(pos1, pos2):
                val = sorted_nums[j]
                for idx in index_map[sorted_nums[j]]:
                    if abs(idx - i) <= k:
                        return True
            bisect.insort(sorted_nums, nums[i])
            if nums[i] not in index_map:
                index_map[nums[i]] = [i]
            else:
                index_map[nums[i]].append(i)
        return False

# a little bit improvement by using deque
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        import bisect
        from collections import deque
        sorted_nums = []
        index_map = {}
        for i in range(len(nums)):
            pos1 = bisect.bisect_left(sorted_nums, nums[i] - t)
            pos2 = bisect.bisect_right(sorted_nums, nums[i] + t)
            for j in range(pos1, pos2):
                val = sorted_nums[j]
                for idx in index_map[sorted_nums[j]]:
                    if abs(idx - i) <= k:
                        return True
            bisect.insort(sorted_nums, nums[i])
            if nums[i] not in index_map:
                q = deque()
                q.append(i)
                index_map[nums[i]] = q
            else:
                index_map[nums[i]].append(i)
            if i > k:
                index_map[nums[i-k-1]].popleft()
        return False

# time: O(nlgk)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        import bisect
        sorted_nums = []
        for i in range(len(nums)):
            pos1 = bisect.bisect_left(sorted_nums, nums[i] - t)
            pos2 = bisect.bisect_right(sorted_nums, nums[i] + t)
            if pos2 > pos1:
                return True
            bisect.insort(sorted_nums, nums[i])
            if i >= k:
                sorted_nums.remove(nums[i-k])
        return False
# time: O(n)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        mapping = {}
        for i in range(len(nums)):
            bucket = nums[i] / (t+1)
            if bucket in mapping or (bucket-1 in mapping and nums[i] - mapping[bucket-1] <= t) or (bucket+1 in mapping and mapping[bucket+1] - nums[i] <= t):
                return True
            mapping[bucket] = nums[i]
            if i >= k:
                del mapping[nums[i-k] / (t+1)]
        return False

