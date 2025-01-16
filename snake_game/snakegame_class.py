import random
import click
import os

class Snake:
    def __init__(self,size):
        self.x = 0
        self.y = 0
        
        self.generate_pos(size)
    
    def generate_pos(self, size):
        self.x = random.randint(0, size.width - 1)
        self.y = random.randint(0, size.height - 1)
    
class User:
    def __init__(self, size):
        self.x = 0
        self.y = 0
        self.w = size.width
        self.h = size.height
        
    def left(self):
        if self.x != 0:
            self.x -= 1
    def up(self):
        if self.y != 0:
            self.y -= 1
    def right(self):
        if self.x < self.w - 1:
            self.x += 1
    def down(self):
        if self.y < self.h -1:
            self.y += 1
            
class Board:
    def __init__(self, size, snake_x, snake_y):
        self.w = size.width
        self.h = size.height
        self.snake_x = snake_x
        self.snake_y = snake_y
    
    def display(self,user_x,user_y):
        count = 3 * self.w + self.w + 1
        print("-" * count)
        for i in range(self.h):
            print("", end="| ")
            for j in range(self.w):
                if (i == self.snake_y) and (j == self.snake_x) == 1:
                    print("X", end=" | ")
                elif (i == user_y) and (j == user_x):
                    print("O", end=" | ")
                else:
                    print(" ", end=" | ")
            print("")
            print("-" * count)

class Size:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        
size = Size(7,7)
user = User(size)
s = Snake(size)
board = Board(size, s.x, s.y)

os.system("cls")
while True:
    board.display(user.x,user.y)

    if s.x == user.x and s.y ==user.y:
        print("축하합니다.")
        break
        
    key = click.getchar()
    if key == "a":
        user.left()
    elif key == "w":
        user.up()
    elif key == "s":
        user.down()
    elif key == "d":
        user.right()
    else:
        pass
    
    os.system("cls")
# s = Snake()
# s.generate_pos(5,3)
# print(s.x, s.y)