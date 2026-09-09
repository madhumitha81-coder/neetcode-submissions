class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums.sort()

        a = []

        i = 0
        while i < len(nums):
            cnt = 1

            while i + cnt < len(nums) and nums[i] == nums[i + cnt]:
                cnt += 1

            a.append((nums[i], cnt))
            i += cnt

        a.sort(key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(a[i][0])

        return ans