def solution(n):
    answer = 0
    N = list(str(n))
    for i in range(len(N)):
        answer += int(N[i])
    return answer


