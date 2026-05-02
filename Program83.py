from collections import Counter

class StringFrequencySorter:
    def __init__(self, s):
        self.s = s

    def sort_by_frequency(self):
        freq_map = Counter(self.s)
        
        sorted_chars = sorted(
            freq_map.items(), 
            key=lambda item: (item[1], item[0])
        )
        
        result = []
        for char, count in sorted_chars:
            result.append(char * count)
            
        return "".join(result)

if __name__ == "__main__":
    test_cases = ["geeksforgeeks", "abc"]
    
    for test in test_cases:
        sorter = StringFrequencySorter(test)
        print(f"Input: {test}")
        print(f"Output: {sorter.sort_by_frequency()}")
        print("-" * 20)