'''
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
'''
# O(n^3), TLE

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        n = len(nums)
        for i in range(1, n-5):
            for j in range(i+2, n-3):
                if presum[i] - presum[0] != presum[j] - presum[i+1]:
                    continue
                for k in range(j+2, n-1):
                    if presum[k] - presum[j+1] != presum[i] - presum[0]:
                        continue
                    if presum[i] - presum[0] == presum[j] - presum[i+1] and presum[j] - presum[i+1] == presum[k] - presum[j+1] and presum[k] - presum[j+1] == presum[n] - presum[k+1]:
                        return True
        return False

# O(n^2)

class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        n = len(nums)
        for j in range(3, n-3):
            hashset = set()
            for i in range(1, j-1):
                if presum[i] == presum[j] - presum[i+1]:
                    hashset.add(presum[i])
            for k in range(j+2, n-1):
                if presum[n] - presum[k+1] == presum[k] - presum[j+1] and presum[n] - presum[k+1] in hashset:
                    return True
        return False

