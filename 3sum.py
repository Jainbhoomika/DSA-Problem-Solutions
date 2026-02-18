#Not an Optimal Solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = []
        n = len(nums)
        for i in range(n-2): #i=0-4 1  
            for j in range(i+1,n-1): #j=0-5 0
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0: 
                        result.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        seen = set()
        unique_elements = []
        for sublist in result:
            if sublist not in seen:
                unique_elements.append(sublist)
                seen.add(sublist)
        return unique_elements
