# 혼자서 하는 틱택토 
# https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 규칙에 따른 적합한 게임인지 확인

def check_game_end(board, str1) : # 0 : 틱택토 완성 X, 1 : 틱택토 완성 O
    
    for i in range(3): 
        # 일직선 가로
        if board[i][0] == board[i][1] == board[i][2] == str1 : 
            return 1
        # 일직선 세로
        if board[0][i] == board[1][i] == board[2][i] == str1 : 
            return 1
    
    # 대각선 왼쪽, 오른쪽
    for i in [0,2] : 
        if board[i][0] == board[1][1] == board[2-i][2] == str1 :
            return 1
        
    return 0

def solution(board):
    answer = -1
    
    # 선공 후공 여부 check
    board_count = ''.join(board)
    board_O = board_count.count("O")
    board_X = board_count.count("X")
    
    if (board_O - board_X) not in [0, 1] : # 1. 선공이 후공과 같거나 1개가 더 많지 않다면 적합하지 않음.
        return 0
    
    else : 
        if check_game_end(board, "O") : # 2. 선공이 이겼을 때
            if check_game_end(board, "X") or board_O == board_X: # 2-1 후공이 완성을 하거나 한번 더 진행을 했다면 적합하지 않음.
                return 0
        
        else : 
            if check_game_end(board, "X") : # 2 선공이 이기지 못하고 후공이 이겼을 때
                if board_O != board_X : # 2-2 후공이 이겼는데 선공이 한번 더 공격했거나 덜 공격했다면 적합하지 않음.
                    return 0

    return 1

# Tic-Tac-Toe
# 선공 후공에 대한 의문 
# 승리 후에도 게임을 진행한 경우 
# 게임판 정보에 대해 나올수 있는 게임상황이라면 1, 아니라면 0

# 선공 후공 => O = X + 1 => 1
# 승리후에도 게임을 진행 => 3개가 일직선인데도 했는가 
# 승리 시 추가로 공격을 진행했는가 => 2 