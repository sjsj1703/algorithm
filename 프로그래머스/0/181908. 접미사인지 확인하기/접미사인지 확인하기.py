def solution(my_string, is_suffix):
    if is_suffix in my_string[-len(is_suffix):]:
        return 1
    return 0