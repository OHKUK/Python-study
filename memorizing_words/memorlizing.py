import click
import os

def read_pass_list(file_name):
    word_list = [ ]
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            word_list.append(line.strip())
    return word_list

def read_meaningful_line(f):
    while True:
        line = f.readline()
        if line == "":
            return ""

        if line[0] == '"':
            continue

        line = line.split(",")
        if len(line) < 3:
            continue

        if len(line[0]) < 2 or len(line[1]) < 2:
            continue

        if not line[0].isalpha() :
            continue

        if line[0] in word_list:
            continue

        return line

os.system("cls")
word_list = read_pass_list('pass.txt')

with open('wordbook.csv', 'r') as f:
    line = f.readline()

    exit_flag = False

    while not exit_flag:
        line = read_meaningful_line(f)
        if line == "":
            break

        answer_flag = True
        while True:
            if answer_flag :
                print(line[1].replace("|", " "))
            else:
                print(line[0])

            print("")
            if answer_flag :
                print("1) 단어확인")
            else:
                print("1) 문제확인")
            print("2) 암기완료")
            print("3) 다음단어")
            print("4) 종료하기")

            sel = click.getchar()
            os.system("cls")

            if sel == "1" :
                answer_flag = not answer_flag
            elif sel == "2":
                with open("pass.txt", "a") as pass_file:
                    pass_file.write(line[0] + "\n")
                break
            elif sel == "3":
                break
            else:
                exit_flag = True
                print("프로그램을 종료합니다.")
                print("감사합니다.")
                break