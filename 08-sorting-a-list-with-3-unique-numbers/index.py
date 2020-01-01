def sortNums(nums):
  counts = {}
# loops through nums array...
  for n in nums:
    # ex: counts[3] = counts.get(3,0)+1
    # if key is not found counts[3] = 0 + 1
    # if key is found, add one to current value
    counts[n] = counts.get(n, 0) + 1
# make an array with counts[1] number of 1's, etc.
  return ([1] * counts.get(1, 0) +
          [2] * counts.get(2, 0) +
          [3] * counts.get(3, 0))


print sortNums([3, 3, 2, 1, 3, 2, 1])