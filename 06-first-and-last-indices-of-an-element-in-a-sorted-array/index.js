var searchRange = function (nums, target) {
    binarySearch = first => {
        let min = 0
        let max = nums.length - 1
        while (true) {
            if (min > max) return -1
            let mid = Math.floor(min + (max - min) / 2)
            if (first) {
                if ((mid === 0 || target > nums[mid - 1])
                    && nums[mid] === target)
                    return mid
                if (target > nums[mid]) {
                    min = mid + 1
                } else {
                    max = mid - 1
                }
            } else {
                if ((mid === nums.length || target < nums[mid + 1])
                    && nums[mid] === target) {
                    return mid
                }
                if (target < mid) {
                    max = mid - 1
                } else {
                    min = mid + 1
                }
            }
        }
    }
    let first = binarySearch(true)
    let last = binarySearch(false)
    if (nums.length > 1) return [first, last]
    else if (nums[0] === target) return [first,first]
    else return [-1,-1]
};


arr = [1, 3, 3, 5, 7, 8, 9, 9, 15]
x = 9
console.log(searchRange(arr, x))