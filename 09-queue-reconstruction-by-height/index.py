class Solution:
  def reconstructQueue(self, people):
    # key arg customize behavior (ex. key=len)
    # lambda -> arguments: expression
    # so the line below reverse sorts first index 
    # and sorts second normally 
    people.sort(key=lambda x: (-x[0], x[1])) #O(nlogn)
    res = []
    for p in people: #O(n)
          res.insert(p[1], p) #O(n)
    return res

  # Time Complexity O(ns^2)
  # Space : O(n)

print(Solution().reconstructQueue(
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]