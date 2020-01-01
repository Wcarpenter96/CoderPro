var twoSum = function (nums, target) {
    dict = {}
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in dict)
            return [dict[target - nums[i]], i]
        dict[nums[i]] = i
    }
    return []
};

console.log(twoSum([2, 7, 11, 15],26))