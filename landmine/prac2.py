import random

def display(m, u):
    for i in range( len(m) ):
        for j in range( len(m[i] )):
            if u[i][j] == 1 :
                print(m[i][j], end=" ")
            else:
                print("*", end=" ")
        print("")

def update_user_map(u):
    # 입력 방법 0 0
    user = input ("> ")
    # ["0", "0"]
    pos_list = user.split(" ")
    row = int(pos_list[0])
    col = int(pos_list[1])
    u[row][col] = 1

def detect_mine(u, m):
    mine_detect_falg = False
    for i in range(len(u)):
        for j in range(len(u[i])):
            if (u[i][j] == 1) and (m[i][j] == 1):
                mine_detect_falg = True
    return mine_detect_falg

m = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

u = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

pos_y = random.randint(0,4)
pos_x = random.randint(0,4)
m[pos_y][pos_x] = 1
print(pos_y,pos_x)

for i in range(3):
    update_user_map(u)
    mine_detect_falg = detect_mine(u, m)
    if mine_detect_falg:
        print("축하합니다.")
        break
    else:
        print("실패입니다.")
    display(m, u)