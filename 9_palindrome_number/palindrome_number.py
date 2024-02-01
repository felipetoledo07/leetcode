class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        for i in range(len(x_string)):
            if x_string[i] != x_string[len(x_string) - i - 1]:
                return False
        return True


solution = Solution()

print('Case 1: ', solution.isPalindrome(121))
print('Case 1: ', solution.isPalindrome(-121))
print('Case 1: ', solution.isPalindrome(10))
