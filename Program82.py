class TimeDifferenceCalculator:
    def __init__(self, time_strings):
        self.time_strings = time_strings
        self.total_seconds_in_day = 24 * 60 * 60

    def _convert_to_seconds(self, time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s

    def find_min_difference(self):
        seconds_list = sorted([self._convert_to_seconds(t) for t in self.time_strings])
        
        min_diff = float('inf')
        
        for i in range(len(seconds_list) - 1):
            diff = seconds_list[i+1] - seconds_list[i]
            if diff < min_diff:
                min_diff = diff
        
        wrap_around_diff = (self.total_seconds_in_day - seconds_list[-1]) + seconds_list[0]
        min_diff = min(min_diff, wrap_around_diff)
        
        return min_diff

if __name__ == "__main__":
    example1 = ["12:30:15", "12:30:45"]
    calc1 = TimeDifferenceCalculator(example1)
    print(calc1.find_min_difference())

    example2 = ["00:00:01", "23:59:59", "00:00:05"]
    calc2 = TimeDifferenceCalculator(example2)
    print(calc2.find_min_difference())