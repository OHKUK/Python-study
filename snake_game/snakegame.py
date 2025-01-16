import random
import click
import os

def display(snake_map,user_x,user_y, key):
    count = 3 * len( snake_map[0]) + len(snake_map[0]) + 1
    print("-" * count)
    for i in range(len(snake_map)):
        print("", end="| ")
        for j in range(len(snake_map[i])):
            if snake_map[i][j] == 1:
                print("X", end=" | ")
            elif (i == user_y) and (j == user_x):
                print("O", end=" | ")
            else:
                print(" ", end=" | ")
        print("")
        print("-" * count)
    if key == None:
        val = ""
    elif key == "a":
        val = "←"
    elif key == "w":
        val = "↑"
    elif key == "s":
        val = "↓"
    elif key == "d":
        val = "→"
    print(val * count)



snake_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
snake_y = random.randint(0, len(snake_map[0])-1)
snake_x = random.randint(0, len(snake_map)- 1)
snake_map[snake_y][snake_x] = 1 

user_x = 0
user_y = 0
key = None

while True:
    display(snake_map,user_x,user_y, key)
    
    key = click.getchar()
    if key == "a":
        if user_x > 0:
            user_x = user_x - 1
    elif key == "w":
        if user_y > 0:
            user_y = user_y - 1
    elif key == "s":
        if user_y < len(snake_map)-1:
            user_y = user_y + 1
    elif key == "d":
        if user_x < len(snake_map[0]) -1:
            user_x = user_x + 1
    else:
        pass
    
    if snake_map[user_y][user_x] == 1:
        break
    
    os.system("cls")
print("축하합니다.")


