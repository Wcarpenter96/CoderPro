class Solution:
    def productExceptSelf1(self, nums):
        import functools
        prods = [functools.reduce(lambda x,y: x*y, nums)] * len(nums)
        res = []
        for i,p in enumerate(prods):
            if nums[i] != 0:
                res.append(int(p/nums[i]))
            else:
                res.append(0)
        return res
    # cumulative sum
    def productExceptSelf2(self, nums):
        # nums = [2,3,4,5]
        res = [1] * len(nums) 
        # res = [1,1,1,1]
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
            print(i,res)
            # i=1: [1,1*2,1,1]
            # i=2: [1,1*2,1*2*3,1]
            # i=3: [1,1*2,1*2*3,1*2*3*4]
        right = 1 
        # res = [1,2,6,24]
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
            print(i,res)
            # i=2: right = 5, nums=[1,2,6*5,24]
            # i=1: right = 5*4, nums=[1,2*4*5,6*5,24]
            # i=0: right = 5*4*3, nums=[1*3*4*5,1*2*4*5,6*5,24]
        return res
            


print(Solution().productExceptSelf2([2,3,4,5]))
