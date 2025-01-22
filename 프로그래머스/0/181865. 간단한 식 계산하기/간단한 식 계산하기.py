def solution(binomial):
    result=binomial.split()
    if result[1] == '+':
        return int(result[0])+int(result[2])
    elif result[1] == '-':
        return int(result[0])-int(result[2])
    else:
        return int(result[0])*int(result[2])

    

