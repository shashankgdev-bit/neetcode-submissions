class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        for xy in points:
            a = xy[0]
            b = xy[1]

            distance = a*a + b*b

            heapq.heappush(h, (-distance, a, b))

            if(len(h) > k):
                heapq.heappop(h)
        
        result = []

        for item in h:
            distance, x1, y1 = item
            result.append([x1,y1])

        return result
        