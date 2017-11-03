'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
# sort + two pointers
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue 
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left+1] == nums[left]: 
                        left += 1 
                    while left<right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return results

# hashmap + two loops
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        idx_map = {}
        sum_set = set()
        for i in range(len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = i
        for i in range(2, len(nums)):
            for j in range(1, i):
                residual = 0 - nums[i] - nums[j]
                if residual in idx_map and idx_map[residual] < i and idx_map[residual] < j:
                    tmp_list = [residual, nums[j], nums[i]]
                    tmp_list.sort()
                    s = ','.join(str(val) for val in tmp_list)
                    if s not in sum_set:
                        sum_set.add(s)
                        result.append(tmp_list)
        return result

# hashmap + one loop
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        idx_map = {}
        sum_set = set()
        for i in range(len(nums)):
            for j in range(i):
                tmp = nums[i] + nums[j]
                if tmp not in idx_map:
                    idx_map[tmp] = [(j, i)]
                else:
                    idx_map[tmp].append((j, i))
        for i in range(2, len(nums)):
            residual = 0 - nums[i]
            if residual in idx_map:
                for pair in idx_map[residual]:
                    if pair[1] < i:
                        tmp_list = [nums[pair[0]], nums[pair[1]], nums[i]]
                        tmp_list.sort()
                        s = ','.join(str(val) for val in tmp_list)
                        if s not in sum_set:
                            sum_set.add(s)
                            result.append(tmp_list)
        return result

# invoke twoSum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        idx_map = {}
        sum_set = set()
        for i in range(2, len(nums)):
            pairs = self.twoSum(nums[:i], -nums[i])
            for pair in pairs:
                tmp_list = [pair[0], pair[1], nums[i]]
                tmp_list.sort()
                s = ','.join(str(val) for val in tmp_list)
                if s not in sum_set:
                    sum_set.add(s)
                    result.append(tmp_list)
        return result
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        pairs = []
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                pairs.append((tmp, nums[i]))
            else:
                d[nums[i]] = i
        return pairs
