import click
import os
import datetime

def return_this_book(title):
    copy_data = [  ]
    with open('rent.csv', 'r') as f:
        data = f.readlines()
        for item in data:
            item = item.split(",")
            if title == item[1] and item[3] == "":
                now     = datetime.datetime.now()
                start   = datetime.datetime.strptime(item[2], "%Y-%m-%d")
                elapsed = now - start
                item[3] = now.strftime("%Y-%m-%d")
                item[4] = f"{elapsed.days * 100}" + "\n"
            copy_data.append(item)

    with open('rent.csv', 'w') as f:
        for item in copy_data:
            # ['김철수', 'Do it 점프 투 파이썬',]
            # '김철수 Do it 점프 투 파이썬'
            item = ",".join(item)
            f.write(item)

def search():
    while True:
        print("검색어를 입력하세요")
        target = input("> ")
        os.system("cls")

        result = []
        with open('book.csv', 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                line = line.split(",")
                if target in line[1] :
                    result.append(line[1].strip())

        length = len(result)
        print("0. 재검색")
        for i in range( min(length, 4)  ):
            print(f"{i+1}. {result[i]}")
        sel = click.getchar()
        os.system("cls")
        if sel == "0":
            continue
        else:
            idx = int(sel) - 1
            break

    return result[idx]

def can_i_borrow(title):
    with open('rent.csv', 'r') as f:
        data = f.readlines()
        for item in data:
            item = item.split(",")
            if item[1] == title and item[3] == "":
                return False
    return True

def borrow():
    while True:
        title = search()
        valid = can_i_borrow(title)
        if valid:
            break

    with open('book.csv', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line == "":
                break

            line = line.split(",")
            if line[1].strip() == title:
                print(f"※※※ {title} ※※※")
                print(f"{line[4]} {line[5]}")
                print(line[10])
                break

    print("1. 대여")
    print("2. 취소")
    sel = click.getchar()
    os.system("cls")
    if sel == "1":
        name = input("회원 이름: ")
        os.system("cls")
        now = datetime.datetime.now()
        with open('rent.csv', 'a') as f:
            f.write(f"{name},{title},{now.strftime('%Y-%m-%d')},," + "\n")

def report():
    title = search()
    with open('rent.csv', 'r') as f:
        acc_price = 0
        for item in f.readlines():
            item = item.split(',')

            if item[1] == title and item[3] != "":
                name = item[0]
                start = datetime.datetime.strptime(item[2], "%Y-%m-%d")
                end   = datetime.datetime.strptime(item[3], "%Y-%m-%d")
                price = int(item[4].strip())

                elapsed = end - start

                print(f"{title} {name} {item[2]} ({elapsed.days}) {price}원")
                acc_price += price

        print("-" * 20)
        print(f"수입 : {acc_price}")

os.system("cls")

while True:
    print("1) 회원가입")
    print("2) 대여하기")
    print("3) 반납하기")
    print("4) 조회하기")
    print("5) 종료")

    sel = click.getchar()
    os.system("cls")
    if sel == "1":
        name  = input("이름 : ")
        phone = input("전화 : ")
        os.system("cls")
        now   = datetime.datetime.now()

        with open("user.csv", "a") as f:
            f.write(f"{name},{now.strftime('%Y-%m-%d')},{phone}"+"\n")

    elif sel == "2":
        borrow()

    elif sel == "3":
        title = search()
        return_this_book(title)

    elif sel == "4":
        report()

    else :
        print("이용해 주셔서 감사합니다.")
        break
