# Runtime Complexity: O(N^2)
# Spacetime Complexity: O(1)

# Intuition: Every palindrome has a center of length one or two. 
# 1) Iterate through string and expand around each center.
# 2) If valid palindrome is created, update max length.
# 3) return max length

