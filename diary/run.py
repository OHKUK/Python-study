import os

def read_db():
    diary = { }
    with open("db.csv", "r") as f:
        for line in f.readlines():
            date = line.split(", ")
            diary[date[0]] = date[1].strip()
    return diary

def write_db(diaty):
    with open("db.csv", "w") as f:
        for date, msg in diary.items():
            f.write(f"{date}, {msg}" + "\n")
    

diary = read_db()

    
while True:
    print("1) 일기 작성")
    print("2) 일기 조회")
    print("3) 종료")
    sel = input("> ")
    
    if sel == "1":
        date = input("날짜:")
        msg = input(">")
        diary[date] = msg
    
    elif sel == "2":
        date = input("날짜:")
        print(diary[date])
    elif sel == "3":
        print("프로그램 종료")
        break
    else:
        print("error")
    
    print("press enter to continue")
    input()
    os.system("cls")


write_db(diary)

# with open("db.csv", "w") as f:
#     date = input("날짜:")
#     msg = input(">")
#     f.write(f"{date}, {msg}" + "\n")

# with open("db.csv", "r") as f:
#     for line in f.readlines():
#         data = line.split(", ")
#         print(data[0], data[1])