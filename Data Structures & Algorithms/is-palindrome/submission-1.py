class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_characters = []
        for char in s:
            if char.isalnum():
                clean_characters.append(char.lower())

        clean_s = "".join(clean_characters)

        if clean_s == clean_s[::-1]:
            return True
        else:
            return False