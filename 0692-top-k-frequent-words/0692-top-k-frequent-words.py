from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)

        # res = sorted(freq, key=lambda x: (-freq[x], x))
        # return res[:k]

        heap = [(-count, word) for word, count in freq.items()]
        
        heapq.heapify(heap) 
        
        return [heapq.heappop(heap)[1] for _ in range(k)]