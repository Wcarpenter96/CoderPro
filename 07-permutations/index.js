var permute = function(nums) {
    const res = [];
    function backtrack(start) {
        if (start === nums.length - 1) {
            res.push(nums.slice(0));
            return;
        }
        for (let i = start; i < nums.length; i++) {
            [nums[i], nums[start]] = [nums[start], nums[i]];
            backtrack(start + 1);
            [nums[i], nums[start]] = [nums[start], nums[i]];
        }
    }
    backtrack(0);
    return res;
};


console.log(permute([1, 2, 3, 4]))
