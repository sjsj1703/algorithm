def solution(myString, pat):
    new=[]
    for i in range(len(myString)):
        if myString[i]=='A':
            new+='B'
        if myString[i]=='B':
            new+='A'
    new2=''.join(new)
    if pat in new2:
        return 1
    return 0