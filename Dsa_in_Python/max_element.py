# Find the Maximum Element (Array)

def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([2, 7, 3, 9, 1]))  # Output: 9
