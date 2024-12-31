def solution(num_list):
    answer = num_list
    if num_list[-1:]>num_list[-2:-1]:
        answer.append(num_list[-1:][0]- num_list[-2:-1][0])
    else:
        answer.append(num_list[-1:][0]*2)
    return answer