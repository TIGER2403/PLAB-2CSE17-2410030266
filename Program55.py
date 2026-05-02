class SubarrayCounter:
    def __init__(self, arr):
        self.arr = arr
    def count_valid(self):
        n = len(self.arr)
        stack = []
        res = 0
        for i in range(n):
            while stack and self.arr[stack[-1]] > self.arr[i]:
                stack.pop()
            if not stack:
                length = i + 1
            else:
                length = i - stack[-1]
            res += length
            stack.append(i)
        return res
arr = list(map(int, input().split()))
obj = SubarrayCounter(arr)
print(obj.count_valid())