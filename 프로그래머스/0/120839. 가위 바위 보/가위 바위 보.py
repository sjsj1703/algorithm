def solution(rsp):
    m=list(rsp)
    answer=[]
    for i in range(len(m)):
        if m[i]=='2':
            answer.append('0')
        elif m[i]=='0':
            answer.append('5')
        else:
            answer.append('2')
    return ''.join(answer)