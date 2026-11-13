class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        counts1 = {}
        counts2 = {}

        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
            counts2[s2[i]] = 1 + counts2.get(s2[i], 0)

        if counts1 == counts2:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            counts2[s2[right]] = 1 + counts2.get(s2[right], 0)
            counts2[s2[left]] -= 1

            if counts2[s2[left]] == 0:
                del counts2[s2[left]]

            left += 1
            if counts1 == counts2:
                return True

        return False
