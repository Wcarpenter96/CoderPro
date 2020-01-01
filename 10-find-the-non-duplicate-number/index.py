class Solution(object):
    def singleNumber(self, nums):
        # create a dictionary 
        occurrence = {}
        # iterate through the dictionary
        for n in nums:
            # insert/increment number key 
            occurrence[n] = occurrence.get(n, 0) + 1
        # .items() returns list with all dictionary keys with values
        # loop through array of key-valued pairs
        for key, value in occurrence.items():
            # return key if value is 1
            if value == 1:
                return key

    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n 
            print unique
        return unique 

print Solution().singleNumber2([4,3,2,4,1,3,2])

# 0^4=4 
# 4^3=7
# 7^2=5 
# 5^4=1 
# 1^1=0 
# 0^3=3 
# 3^2=1 