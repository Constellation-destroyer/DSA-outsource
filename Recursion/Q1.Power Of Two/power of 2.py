class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
sol = Solution()
n = 1
print(sol.isPowerOfTwo(n))
