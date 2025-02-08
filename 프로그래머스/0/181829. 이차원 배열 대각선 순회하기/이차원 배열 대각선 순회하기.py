def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(min(len(board[i]), k - i + 1)):
            answer+=board[i][j]
    return answer