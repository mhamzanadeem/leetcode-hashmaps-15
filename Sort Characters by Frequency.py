class Solution:
    def frequencySort(self, s: str) -> str:
        string_frequency = Counter(s)
        return ''.join(
            char * frequency
            for char, frequency in string_frequency.most_common()
        )