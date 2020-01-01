/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    res = []
    for (let i = 0; i < nums.length; i++) {
        res.push(1)
    }
    for (let i = 1; i < nums.length; i++) {
        res[i] = res[i-1] * nums[i-1]
    }
    let right = 1
    for (let i = nums.length - 2; i > -1; i--) {
        right *= nums[i+1]
        res[i] *= right 
    }
    return res
};

console.log(productExceptSelf([2,3,4,5]))