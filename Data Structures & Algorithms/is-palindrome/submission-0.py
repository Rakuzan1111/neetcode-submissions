class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for character in s:
            if character.isnumeric():
                new_s += character
            elif character.isalpha():
                new_s += character.lower()
        i1 = 0
        i2 = len(new_s) - 1
        while i1 < i2:
            if new_s[i1] ==  new_s[i2]:
                i1 += 1
                i2 -= 1
            else:
                return False
        return True

