# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# To reach step n, you could have come from step n-1 (by climbing 1 step) or step n-2 (by climbing 2 steps).
# So, the total ways to reach step n is the sum of ways to reach n-1 and n-2.

# ways(n) = ways(n-1) + ways(n-2)
# This is similar to the Fibonacci sequence.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first, second = 1, 2
        
        for _ in range(3, n + 1):
            first, second = second, first + second
            
        return second
    
Solution().climbStairs(5)  # Output: 8

print(Solution().climbStairs(5))