def solution(my_string, alp):
    answer=[]
    for i in my_string:
        if i ==  alp:
            answer.append(alp.upper())
        else:
            answer.append(i)
    return ''.join(answer)