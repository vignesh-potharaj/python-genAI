def find_first(arr, target):
    low = 0
    high = len(arr) - 1
    first_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_index = mid
            high = mid - 1 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_index

def find_last(arr, target):
    low = 0
    high = len(arr) - 1
    last_index = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last_index = mid
            low = mid + 1 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last_index

def count_occurrences(arr, target):
    first = find_first(arr, target)
    if first == -1:
        return 0 
    last = find_last(arr, target)
    return last - first + 1


input_array = [1, 2, 2, 2, 3, 4]
target_value = 2
count = count_occurrences(input_array, target_value)
print(f"Input: {input_array}, target = {target_value}")
print(f"Output: {count}") 
