height = [6,4,3,1,4,6,99,62,1,2,6]

class Solution:
    
    def maxArea(self, height):
        i, j = 0, len(height)-1
        
        max_area = 0

        for n in sorted(set(height)):
            while height[i] < n: i += 1
            while height[j] < n: j -= 1
            max_area = max((j-i)*n, max_area)

        return max_area

    def maxArea2(self, height):
        i, j = 0, len(height)-1
        
        max_area = min(height[i], height[j]) * (j-i)

        while i < j:
            if height[i] < height[j]: i += 1
            else: j -= 1
            max_area = max(max_area, min(height[i], height[j]) * (j-i))

        return max_area

s = Solution()
print(s.maxArea2(height))
