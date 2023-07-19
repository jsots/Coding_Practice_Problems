class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                # greater than becasue dealing with negatives, need to keep this in mind when dealing with these values. note the subtraction as well. alternatively, could take the abs of them and deal with that. 
                heapq.heappush(stones, first - second)

        if stones:
            return abs(stones[0])
        else:
            return 0


