const findPythagoreanTriplets = nums => {
  let squares = new Set(nums.map(x => x * x));
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (squares.has(nums[i] * nums[i] + nums[j] * nums[j])) {
        return true;
      }
    }
  }
};

console.log(findPythagoreanTriplets([3, 4, 12, 5, 13]));
