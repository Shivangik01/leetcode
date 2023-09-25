from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)

        res = sorted(freq, key=lambda x: (-freq[x], x))
        return res[:k]