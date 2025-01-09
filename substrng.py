class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if word.endswith(pref):
                count += 1
        return count

# Example usage
solution = Solution()
words1 = ["pay", "attention", "practice", "attend"]
pref1 = "n"
print(solution.prefixCount(words1, pref1))  # Output: 2

words2 = ["leetcode", "win", "loops", "success"]
pref2 = "s"
print(solution.prefixCount(words2, pref2))  # Output: 0
