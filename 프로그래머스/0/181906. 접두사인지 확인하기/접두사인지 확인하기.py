def solution(my_string, is_prefix):
    if is_prefix in my_string[0:len(is_prefix)]:
        return 1
    return 0