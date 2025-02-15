def solution(arr):
    i = 1
    while i < len(arr): 
        i *= 2
    while len(arr) < i: 
        arr.append(0)

    return arr