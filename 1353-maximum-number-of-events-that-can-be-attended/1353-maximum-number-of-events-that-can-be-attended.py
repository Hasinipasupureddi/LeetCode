class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        day = 1
        i = 0
        n = len(events)
        attended = 0
        while i < n or min_heap:
            # add all events starting today
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            # remove expired events
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            # attend event ending earliest
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
            day += 1
        return attended