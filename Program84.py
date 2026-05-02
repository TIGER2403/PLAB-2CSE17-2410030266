class LengthSorter:
    def __init__(self, arr):
        self.arr = arr

    def sort_by_length(self):
        self.arr.sort(key=len)
        return self.arr

if __name__ == "__main__":
    example1 = ["GeeksforGeeeks", "I", "from", "am"]
    sorter1 = LengthSorter(example1)
    print(sorter1.sort_by_length())

    example2 = ["You", "are", "beautiful", "looking"]
    sorter2 = LengthSorter(example2)
    print(sorter2.sort_by_length())