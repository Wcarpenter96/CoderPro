class Solution:
  def permute(self, nums):
        res = []
        def permuteHelper(start):
            # If starting index is at the end of array,
            # make a copy of nums and append it to res
            if start == len(nums) - 1:
                print(nums)
                res.append(nums[:])
            for i in range(start, len(nums)):
                # swap 
                nums[start], nums[i] = nums[i], nums[start]
                # call recursively until you get to end of array 
                permuteHelper(start + 1)
                # swap back
                nums[start], nums[i] = nums[i], nums[start]
        permuteHelper(0)
        return res

print(Solution().permute([1, 2, 3]))