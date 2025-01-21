import os
import click

class MyFile:
    def __init__(self, fname, mode):
        self.f = open(fname, mode)
        self.mode = mode

    def 암기_리스트_가져오기(self):
        if self.mode == 'w':
            print("잘못된 호출입니다.")
        else:
            data = self.f.readlines()
            return [ x.strip() for x in data ]

    def 암기_단어_쓰기(self, word):
        if self.mode == 'r':
            print("잘못된 호출입니다.")
        else:
            self.f.write(word + "\n")

    def 단어셋_가져오기(self, word_list):
        while True:
            line = self.f.readline()
            if line == "":
                Vocap("", "")

            if line[0] == '"':
                continue

            line = line.split(",")
            if len(line) < 3:
                continue

            if len(line[0]) < 2 or len(line[1]) < 2:
                continue

            if not line[0].isalpha() :
                continue

            if line[0] == "단어":
                continue

            if line[0] in word_list:
                continue

            return Vocap(line[0], line[1])


    def __del__(self):
        self.f.close()

class Vocap:
    def __init__(self, word, meaning):
        self.w = word
        self.m = meaning.replace("|", " ")

pass_txt = MyFile("pass.txt", "r")
word_list = pass_txt.암기_리스트_가져오기()

wordbook = MyFile("wordbook.csv", "r")

exit_flag = False

while not exit_flag:
    vocap = wordbook.단어셋_가져오기(word_list)
    if vocap.w == "":
        break

    answer_flag = True

    while True:
        if answer_flag :
            print(vocap.m)
        else:
            print(vocap.w)
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
            mf_pass = MyFile("pass.txt", "w")
            mf_pass.암기_단어_쓰기(vocap.w)
            word_list.append(vocap.w)
        elif sel == "3":
            break
        else:
            exit_flag = True
            print("프로그램을 종료합니다.")
            print("감사합니다.")
            break




