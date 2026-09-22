class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = s.lower()
        chars = []

        for char in string:
            if char.isalnum():
                chars.append(char)

        cleaned = "".join(chars)

        if cleaned == cleaned[::-1]:
            return True
        else:
            return False

