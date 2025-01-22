
class BookList:
    def __init__(self, title, price, pubdate, desc):
        self.title = title
        self.price = price
        self.date = pubdate
        self.desc = desc

    def __repr__(self):
        str  = f"※※※※ {self.title} ※※※※" + "\n"
        str += f"{self.date} {self.price}\n"
        str += f"{self.desc}"
        return str

class UserInfo:
    def __init__(self, name, date, phone):
        self.name = name
        self.date = date
        self.phone = phone

class RentHist:
    def __init__(self, name, title, borrow_date, return_date):
        self.name = name
        self.title = title
        self.borrow_date = borrow_date
        self.return_date = return_date

# b = BookList("abc", 1000, "20210101", "hello world")
# print(b)