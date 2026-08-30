import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = abs(heapq.heappop(heap))
            second = abs(heapq.heappop(heap))

            if first != second:
                heapq.heappush(heap, -(first - second))

        return abs(heap[0]) if heap else 0
        