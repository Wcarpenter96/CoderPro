/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
  let idx = null;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] > nums[i + 1]) {
      if (idx != null) {
        return false;
      }
      idx = i;
    }
  }
  if (
    idx == 0 ||
    idx == nums.length - 2 ||
    nums[idx] <= nums[idx + 2] ||
    nums[idx - 1] <= nums[idx + 1]
  ) {
    return true;
  }
  return false;
};
