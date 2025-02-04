def solution(num, k):
    for i in range(num):
        if str(k) in str(num):
            return str(num).index(str(k))+1
        else:
            return -1