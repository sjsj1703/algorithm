def solution(num_list):
    result1=''
    result2=''
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            result1+=(str(num_list[i]))
        else:
            result2+=(str(num_list[i]))
    return int(result1)+int(result2)