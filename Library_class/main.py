from bookmanager import BookStoreManager
import click
import os


bsm = BookStoreManager()

while True:
    print("1. 회원가입")
    print("2. 도서대여")
    print("3. 도서반납")
    print("4. 조회하기")
    print("5. 종료")
    sel = click.getchar()

    if sel == "1":
        bsm.register()
    elif sel == "2":
        bsm.rent()
    elif sel == "3":
        bsm.return_book()
    elif sel == "4":
        bsm.report()
    elif sel == "5":
        print("이용해 주셔서 감사합니다.")
        break

    print("press enter to continue")
    input("")
    os.system("cls")