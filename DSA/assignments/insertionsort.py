def insertion_sort_exams(scores):
    n = len(scores)
    shifts = 0
    arr = scores[:]
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] 
            j -= 1
            shifts += 1
        arr[j + 1] = key
        
    return arr, shifts
scores = [72, 45, 88, 60, 95]
print(insertion_sort_exams(scores))
