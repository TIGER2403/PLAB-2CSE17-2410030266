class StringPairCounter:
    def __init__(self, arr):
        self.arr = arr

    def count_pairs(self):
        count = 0
        patterns = {}
        
        for s in self.arr:
            for i in range(len(s)):
                pattern = s[:i] + '*' + s[i+1:]
                
                if pattern in patterns:
                    count += patterns[pattern]
                    patterns[pattern] += 1
                else:
                    patterns[pattern] = 1
                    
        return count

if __name__ == "__main__":
    example1 = ["abc", "abd", "bbd"]
    solver1 = StringPairCounter(example1)
    print(solver1.count_pairs())

    example2 = ["def", "deg", "dmf", "xef", "dxg"]
    solver2 = StringPairCounter(example2)
    print(solver2.count_pairs())
    
    example3 = ["bcde", "bced", "bdce"]
    solver3 = StringPairCounter(example3)
    print(solver3.count_pairs())