class WorkerCoverage:
    def __init__(self, arr):
        self.arr = arr

    def min_people(self):
        n = len(self.arr)
        intervals = []
        for i, r in enumerate(self.arr):
            if r != -1:
                l = max(0, i - r)
                rr = min(n - 1, i + r)
                intervals.append((l, rr))

        intervals.sort()
        res = 0
        i = 0
        curr_end = 0
        farthest = 0

        while curr_end < n:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1
            if farthest == curr_end:
                return -1
            curr_end = farthest
            res += 1

        return res


arr = list(map(int, input().split()))
obj = WorkerCoverage(arr)
print(obj.min_people())