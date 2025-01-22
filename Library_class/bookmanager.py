import os
import click
from bookrw import (RentHistRw, BookListReader, UserInfoRw)

class BookStoreManager:

    def __init__(self):
        self.rh = RentHistRw()

    def register(self):
        name  = input("이름 : ")
        phone = input("전화 : ")
        user = UserInfoRw()
        user.register(name, phone)

    def _search_book_list(self):
        while True:
            word = input("책제목 : ")

            blr = BookListReader()
            book_list = blr.search_titles(word)

            print("0. 재검색")
            for i in range( min(4, len(book_list))):
                print(f"{i+1}. {book_list[i]}")

            sel = click.getchar()
            os.system("cls")
            if sel == "0":
                continue
            else:
                break

        idx = int(sel) - 1
        return book_list[idx]

    def rent(self):
        title = self._search_book_list()

        valid = self.rh.can_i_borrow(title)
        if not valid:
            print("대여 중 입니다.")
            return None
        else:
            name = input("이름 : ")
            self.rh.rent(name, title)

    def return_book(self):
        title = self._search_book_list()
        self.rh.return_this_book(title)

    def report(self):
        title = self._search_book_list()
        self.rh.report(title)

# bsm = BookStoreManager()
# title = bsm._search_book_list()
# print(title)