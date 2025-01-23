def solution(n):
    answer = []
    if n % 2 == 0:  
        answer.extend(range(2, n+1, 2))  
        return sum(x**2 for x in answer)
    else:
        answer.extend(range(1, n+1, 2))  
        return sum(answer)