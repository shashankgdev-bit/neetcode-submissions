import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        groups = defaultdict(int)

        for x in nums:
            groups[x] += 1
        
        h = []

        for key, value in groups.items():
            heapq.heappush(h,(value,key))
            if len(h)>k:
                heapq.heappop(h)
        
        l = []

        for a,b in h:
            l.append(b)

        return l