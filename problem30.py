def row_with_max_1s(arr):
    n = len(arr)
    if n == 0:
        return -1
    m = len(arr[0])
    max_row_index = -1
    row = 0
    col = m - 1
    
    while row < n and col >= 0:
        if arr[row][col] == 1:
            max_row_index = row
            col -= 1
        else:
            row += 1
            
    return max_row_index
