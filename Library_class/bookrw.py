from bookdata import (BookList, UserInfo, RentHist)
import datetime

class BookListReader:
    def search_titles(self, word):
        result = []
        with open('book.csv', 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                line = line.split(",")
                if word in line[1] :
                    result.append(line[1].strip())
        return result

    def search_book(self, title):
        with open('book.csv', 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if line == "":
                    break

                line = line.split(",")
                if title == line[1].strip():
                    b = BookList(title, line[4], line[5], line[10])
                    return b

class UserInfoRw:
    def register(self, name, phone):
        now = datetime.datetime.now()

        with open('user.csv', 'r') as f:
            for item in f.readlines():
                item = item.split(',')
                if (item[0] == name) and (item[2].strip() == phone):
                    return None

        with open('user.csv', 'a') as f:
            f.write(f"{name},{now.strftime('%Y-%m-%d')},{phone}" + "\n")

class RentHistRw:
    def rent(self, name, title):
        with open('rent.csv', 'a') as f:
            now = datetime.datetime.now()
            f.write(f"{name},{title},{now.strftime('%Y-%m-%d')},," + "\n")

    def return_this_book(self, title):
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

    def can_i_borrow(self, title):
        with open('rent.csv', 'r') as f:
            data = f.readlines()
            for item in data:
                item = item.split(",")
                if item[1] == title and item[3] == "":
                    return False
        return True

    def report(self, title):
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

# b = BookListReader()
# book_list = b.search_titles("파이썬")
# bl = b.search_book(book_list[0])
# print(bl)