class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		# create an empty dictionary
		# iterate through the nums list
		# check if each element found in the dictionary
		# if an element is in the dictionary return true 
		# else add element as a key and give value 'True' to the key
		# after iteration if no elements have duplicate return False
		myDict = {}
		n = len(nums)
		for i in range(n):
			if myDict.get(nums[i], False):
				return True
			else:
				myDict[nums[i]] = True
		return False
		