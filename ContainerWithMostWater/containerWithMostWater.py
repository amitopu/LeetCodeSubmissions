class Solution:
	def maxArea(self, height: List[int]) -> int:
		# take two pointer pointing to first element and last element in the height list
		left = 0
		right = len(height) - 1
		maxWaterArea = 0
		
		# calculate water area and check everytime if it is higher than before
		# take the higher value
		# shift the left pionter to right by one if current leftmost height < current rightmost height
		# otherwise shift the right pionter to left by one
		while(left < right):
			maxWaterArea = max(maxWaterArea, min(height[left], height[right]) * (right-left))
			
			if height[left] > height[right]:
				right -= 1
			else:
				left += 1
		return maxWaterArea