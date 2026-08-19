from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        string_count = Counter(s)
        result = ""

        while string_count:
            for char in sorted(string_count):
                result += char
                string_count[char] -= 1

                if string_count[char] == 0:
                    del string_count[char]

            for char in sorted(string_count, reverse=True):
                result += char
                string_count[char] -= 1

                if string_count[char] == 0:
                    del string_count[char]

        return result