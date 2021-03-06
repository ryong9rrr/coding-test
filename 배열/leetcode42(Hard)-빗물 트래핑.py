# 투 포인터 // 56ms
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        if not height:
            return 0
        
        volume = 0
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
                
        return volume


# stack // 52ms
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        stack = deque()
        volume = 0
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if not stack:
                    break
                prev = height[stack[-1]]
                current = height[i]
                distance = i - stack[-1] -1
                waters = min(prev, current) - height[mid]
                volume += distance * waters
                
            stack.append(i)
            
        return volume