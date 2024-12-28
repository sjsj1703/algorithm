def solution(hp):
    n=hp//5
    hp2=hp-(5*n)
    m= hp2//3
    hp3= hp2-(3*m)
    answer = n+m+hp3
    return answer