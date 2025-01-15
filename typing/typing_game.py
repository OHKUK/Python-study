import game
import os

file_list = os.listdir()

txt_list = [ ]
for path in file_list:
    # if path[ -3 : ] == "txt":
    # if path.split(".")[-1] == "txt":
    if path.endswith("txt"):
        txt_list.append(path)
        

count = len(txt_list) + 1

while True:
    for i in range(len(txt_list)):
        file_name = txt_list[i].split(".")[0]
        print(f"{i+1}) {file_name}")
    print("5) 종료")

    sel = input("> ")
    if sel == "5":
        break
    
    idx = int(sel) - 1
    
    game.play_type_game(txt_list[idx])
    
    print("press enter key to continue")
    input()
    
    os.system("cls")