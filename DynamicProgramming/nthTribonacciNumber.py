# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
# optimal Space Complexity: O(1)
    def tribonacciOptimized(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        first, second, third = 0, 1, 1
        
        for _ in range(3, n + 1):
            first, second, third = second, third, first + second + third
            
        return third