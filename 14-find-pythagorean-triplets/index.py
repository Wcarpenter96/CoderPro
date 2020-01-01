def findPythagoreanTriplets1(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a*a + b*b == c*c:
                    return True
    return False


def findPythagoreanTriplets2(nums):
    squares = set([n*n for n in nums])
    for a in nums:
        for b in nums:
            if a*a + b*b in squares:
                return True
    return False

print findPythagoreanTriplets1([3, 4, 12, 5, 13])
print findPythagoreanTriplets2([3, 4, 12, 5, 13])
