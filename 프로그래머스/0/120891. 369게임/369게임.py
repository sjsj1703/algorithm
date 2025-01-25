def solution(order):
    answer=0
    new=str(order)
    for char in new:
        if char in ('3', '6', '9'):
            answer+=1
    return answer