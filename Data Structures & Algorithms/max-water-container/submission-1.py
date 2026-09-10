class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1
        r = 0

        while i < j:
            m = min(heights[i], heights[j]) * (j - i)
            r = max(r, m)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return r