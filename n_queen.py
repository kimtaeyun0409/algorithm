def dfs(num):
    global cnt,chk,board
    if num+1 == n:
        cnt += 1
        return

    for i in range(n):
        if chk[i] == 0:
            board[num] = i
            t = True
            for j in range(num):
                if abs(board[num]-board[num]) == abs(num-j):
                    t = False
                    break
            if t:
                chk[i] = 1
                dfs(num+1)
                chk[i]=0
                

n = int(input())
board = [0 for _ in range(n)]
chk = [0 for _ in range(n)]
cnt = 0


dfs(0)
print(cnt)
