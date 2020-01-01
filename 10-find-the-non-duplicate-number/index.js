var findDuplicate = function (nums) {
    let res;
    let occurence = new Map()
    nums.forEach(n => {
        if (occurence.has(n))
            occurence.set(n, occurence.get(n) + 1)
        else
            occurence.set(n, 0)
    });
    occurence.forEach((value, key) => {
        if (value > 0) 
            res = key
    })
    return res
};

console.log(findDuplicate([4, 1, 2, 5, 5, 5, 3, 9]))