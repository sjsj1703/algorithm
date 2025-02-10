def solution(n):
    for pizza in range(1, n + 1): 
        if (pizza * 6) % n == 0:
            return pizza