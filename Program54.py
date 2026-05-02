class PreviousSmallerElement:
    def __init__(self, arr):
        self.arr = arr

    def compute(self):
        stack = []
        result = []

        for x in self.arr:
            while stack and stack[-1] >= x:
                stack.pop()
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(x)

        return result


arr = list(map(int, input().split()))
obj = PreviousSmallerElement(arr)
print(*obj.compute())