# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
# Time Complexity: O(n)
# Space Complexity: O(n)    

# Optimized Space Complexity: O(1)

    def fibOptimized(self, n: int) -> int:
        if n <= 1:
            return n
        
        a, b = 0, 1
        
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    
print(Solution().fib(10))  # Output: 55
print(Solution().fibOptimized(10))  # Output: 55
# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.