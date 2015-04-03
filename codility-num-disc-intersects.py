#
# Author: Wouter Coppieters
# 
# 1. NumberOfDiscIntersections
# 
# 
# Task description
# Given an array A of N integers, we draw N discs in a 2D plane such that the I-th disc is centered on (0,I) and has a radius of A[I]. We say that the J-th disc and K-th disc intersect if J ≠ K and J-th and K-th discs have at least one common point.
# Write a function:
# def solution(A)
# that, given an array A describing N discs as explained above, returns the number of pairs of intersecting discs. For example, given N=6 and:
# A[0] = 1  A[1] = 5  A[2] = 2 
# A[3] = 1  A[4] = 4  A[5] = 0  
# intersecting discs appear in eleven pairs of elements:
# 0 and 1,
# 0 and 2,
# 0 and 4,
# 1 and 2,
# 1 and 3,
# 1 and 4,
# 1 and 5,
# 2 and 3,
# 2 and 4,
# 3 and 4,
# 4 and 5.
# so the function should return 11.
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
# Assume that:
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2147483647].
# Complexity:
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.
# 
def solution(A):
    from collections import defaultdict
    starts, ends, discs, intersects = [0] * len(A), [0] * len(A), 0, 0
    if not len(A):
        return 0
    for index, radius in enumerate(A):
        left, right = index - radius, index + radius
        starts[max(0,left)] += 1
        ends[min(len(A) - 1,right)] += 1
    
    for i in range(len(A)):
        if starts[i] > 0:
            intersects += discs * starts[i] + (starts[i] * (starts[i] - 1)/2)
            discs += starts[i]
        discs -= ends[i]

    return intersects if intersects <= 10000000 else -1
            

print solution([1, 5, 8, 7, 8, 4, 8, 5, 0, 5])