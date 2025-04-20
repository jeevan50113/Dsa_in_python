# frequency_counter.py
def count_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

print(count_freq([1, 2, 2, 3, 1, 4, 2]))
# Output: {1: 2, 2: 3, 3: 1, 4: 1}
