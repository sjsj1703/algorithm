def solution(my_strings, parts):
    a=''
    for i in range(len(my_strings)):
        a+=my_strings[i][parts[i][0]:parts[i][1]+1]
    return a