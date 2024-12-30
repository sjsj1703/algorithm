def solution(todo_list, finished):
    answer = []

    do_dict=dict(zip(todo_list, finished))
    for task, is_finished in do_dict.items():
        if not is_finished:  
            answer.append(task)
                 
    return answer