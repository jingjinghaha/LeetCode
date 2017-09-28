'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(nˆ2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
# O(nˆ2)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        dp = [1 for i in xrange(len(nums))]
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)

'''
LIS问题是这样描述的：在一个数列中寻找一个序列，使得序列中的任意两个数a[i]和a[j]满足，若i < j，必有a[i] < a[j]。有一个很直接的动态规划思想是：设dp[i]表示以第i个数为结尾的最长递增子序列的长度，则状态转移方程为：dp[i] = max{dp[j] + 1}, 1 <= j < i, a[j] < a[i]，复杂度为O(n2)O(n2)。其实这里还有一个很直接的优化，即：考虑两个数a[x]和a[y], x < y, a[x] < a[y]且dp[x] = dp[y]，那么当dp[t]一样时，显然选取a[x]有可能得到更好的答案。此时可以按照dp[t] = k进行分类，只需保留dp[t] = k的所有a[t]中的最小值。设d[k]记录这个值，则d[k] = min{a[t], dp[t] = k}。

这时注意到d的两个特点：1. d[k]在计算过程中单调不升； 2. d数组是有序的，d[1]<d[2]<..d[n]。
利用这两个性质，可以借助单调队列的思想很方便的求解，设当前已求出的最长上升子序列的长度为len（初始时为1），每次读入一个新元素x，入队规则如下：
1. 若x > d[len]，则直接加入到d的末尾，且len ++；
2. 否则，在d中二分查找，找到第一个比x小的数d[k]，令d[k + 1] = x。
'''
# O(nlgn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        dp = []
        for i in xrange(len(nums)):
            pos = bisect.bisect_left(dp, nums[i])
            if pos < len(dp):
                dp[pos] = nums[i]
            else:
                dp.append(nums[i])
        return len(dp)

