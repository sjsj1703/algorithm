def solution(strArr):
    new=[]
    for i in range(len(strArr)):
        if i%2==1:
            new.append(strArr[i].upper())
        else:
            new.append(strArr[i].lower())
    return new

