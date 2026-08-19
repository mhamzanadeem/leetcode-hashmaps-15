class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        array_frequency = Counter(arr)

        return len(array_frequency.values()) == len(set(array_frequency.values()))