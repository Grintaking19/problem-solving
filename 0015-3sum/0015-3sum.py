class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       result =[]
       for i in range(0,len(nums)-2):
            l, r = i+1 ,len(nums) -1  
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l<r:
                if nums[l] +nums[r] < -nums[i]:
                    l+=1
                elif nums[l] +nums[r] > -nums[i]:
                    r-=1
                else :
                    result.append([nums[i], nums[l] ,nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates for the left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
       return result