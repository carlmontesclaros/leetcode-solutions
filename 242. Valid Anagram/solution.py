class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sorted(s)
        sorted(t)

        if sorted(s) == sorted(t):
            return True

        return False