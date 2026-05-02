class ParenthesesScore:
    def __init__(self, s):
        self.s = s

    def calculate(self):
        stack = [0]

        for ch in self.s:
            if ch == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)

        return stack[0]


s = input().strip()
obj = ParenthesesScore(s)
print(obj.calculate())