# Author: Wouter Coppieters
#
# 1. CountBoundedSlices
#
# An integer K and a non-empty zero-indexed array A consisting of N integers are given.
# A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
# A bounded_slice is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to K. More precisely it is a slice, such that max(A[P], A[P + 1], ..., A[Q]) − min(A[P], A[P + 1], ..., A[Q]) ≤ K.
# The goal is to calculate the number of bounded_slices.
# For example, consider K = 2 and array A such that:
#     A[0] = 3
#     A[1] = 5
#     A[2] = 7
#     A[3] = 6
#     A[4] = 3
# There are exactly nine bounded_slices: (0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4).
# Write a function:
# def solution(K, A)
# that, given an integer K and a non-empty zero-indexed array A of N integers, returns the number of bounded_slices of array A.
# If the number of bounded_slices is greater than 1,000,000,000, the function should return 1,000,000,000.
# For example, given:
#     A[0] = 3
#     A[1] = 5
#     A[2] = 7
#     A[3] = 6
#     A[4] = 3
# the function should return 9, as explained above.
# Assume that:
# N is an integer within the range [1..100,000];
# K is an integer within the range [0..1,000,000,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
# Elements of input arrays can be modified.
# 
def solution(K, A):
    lindex, left = 0, A[0]
    maxi, mini = -float('inf'), float('inf')
    ranges,maxes,mins,overlaps = [],[],[],[]
    max_index = min_index = 0

    for rindex, right in enumerate(A):
        
        maxi, mini, prev_max, prev_min = max(maxi, right), min(mini, right), None, None
        
        while(len(maxes) > max_index and maxes[-1][0] < right): prev_max = maxes.pop()
        while(len(mins) > min_index and mins[-1][0] > right): prev_min = mins.pop()

        maxes.append((right, prev_max[1] if prev_max and prev_max[0] < right else rindex))
        mins.append((right, prev_min[1] if prev_min and prev_min[0] > right else rindex))
        
        if abs(maxi - mini) > K:
            
            ranges.append(rindex - lindex)

            if not maxi == right:
                while max_index < len(maxes) and maxes[max_index][0] > mini + K: max_index += 1
                next_point = maxes[max_index]
                maxi, lindex = next_point
            else:
                while min_index < len(mins) and mins[min_index][0] < maxi - K: min_index += 1
                next_point = mins[min_index]
                mini, lindex = next_point
                
            overlaps.append(rindex - lindex)

    ranges.append(rindex - lindex + 1)

    return min(
                reduce(lambda total, a: total - (a * (a+1))/2, overlaps, 
                reduce(lambda total, a: total + (a * (a+1))/2, ranges, 0)),
            1000000000)

#print solution(6, [2, 2, 3, 3, 9, 8, 5, 1, 7, 4, 6, 10]) #40
#print solution(4, [1, 3, -3, -2, -1, 2, 3, 1, 4]) #23
#print solution(2, [3, 5, 7, 6, 3]) #9
#print solution(5, [2, 3, 2, 9, 8, 3, 10, 6, 7, 1, 10, 9]) #21
#print solution(3, [10, 1, 7, 2, 2, 9, 3, 6, 2, 7, 3, 3]) # 15
#print solution(5, [10, 7, 10, 4, 9, 3, 5, 8, 2, 7, 7, 3]) #25
#print solution(6, [4, 5, 8, 5, 1, 4, 6, 8, 7, 2, 2, 5]) # 44