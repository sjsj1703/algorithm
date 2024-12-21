def solution(my_string):
    m=['a','e','i','o','u']
    list1=list(my_string)
    answer=''
    for i in range(len(list1)):
        if list1[i] in m:
            continue  
        else:
             answer+=list1[i]
    return answer
