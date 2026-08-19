# LeetCode HashMap Problems - 15 Problems

## Link to Solutions + 'When to Reach for a Hashmap' Checklist
- Solutions: https://github.com/yourusername/leetcode-hashmaps-15
- Checklist: https://your-checklist-link.example.com

## Acceptance Criteria
- All 15 problems in the repo folder solved
- Can solve Two Sum in O(n) using a hashmap - brute force is O(n²) because it checks every pair (n×(n-1)/2 comparisons)
- Key design in Group Anagrams: using sorted string (`tuple(sorted(s))`) or char-count array as the hashmap key to group anagrams efficiently

## Notes: When a Hashmap is the Right Tool
1. Fast lookups - checking if an element exists in O(1) instead of O(n)
2. Counting frequencies - tracking how many times each element appears
3. Grouping by key - mapping related items together (e.g., anagrams, two-sum complements)