class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        return_number = 0
        for i in range(len(s)):
            if i != len(s) - 1 and roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
                return_number -= roman_numbers[s[i]]
            else:
                return_number += roman_numbers[s[i]]
        return return_number


solution = Solution()

print('Case 1: ', solution.romanToInt("III"))
print('Case 1: ', solution.romanToInt("LVIII"))
print('Case 1: ', solution.romanToInt("MCMXCIV"))
