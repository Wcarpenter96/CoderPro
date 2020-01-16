class Solution:
    def getRange(self, arr, target):
        first = self.binarySearch(arr, 0, len(arr)-1, target, True)
        last = self.binarySearch(arr, 0, len(arr)-1, target, False)
        return [first, last]
    def binarySearch(self, arr, low, high, target, findFirst):
        while True:
        # If high is less than low, return false
            if high < low:
                return -1
            # ex. for first mid, we have mid = 0 + (8 - 0) // 2 = 4
            # then mid = 5 + (8 - 5) // 2 = 6
            mid = low + (high - low) // 2
            # If we are finding the first instance of target
            if findFirst:
                # if we are at the first index 
                # or the target value is greater than the element before it 
                # AND 
                # element at mid index is our target
                # return it 
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                # if our target is greater than our mid, set the lb to one index above mid
                if target > arr[mid]:
                    low = mid + 1
                # else set our ub to one index lower than mid 
                else: 
                    high = mid - 1
            # If we are finding the last instance of target
            else:
                # if we are at the last index 
                # or the target value is less than the element after it 
                # AND 
                # element at mid index is our target
                # return it 
                if (mid == len(arr)-1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                # if our target is less than the mid, set the ub to one index below the mid
                if target < arr[mid]:
                    high = mid - 1 
                # if our target is greater than the mid, set the lb to one index above the mid
                else: 
                    low = mid + 1
        

arr = [1,3,3,5,7,8,9,9,15]
x = 9
print Solution().getRange(arr, 9)