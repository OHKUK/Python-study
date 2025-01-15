# import language as lg
from language import translate
import time

f = open("Night.Of.The.Living.Dead.1968.txt", "r")

# for line in f.readline():
#     print(line)

while True:
    line = f.readline()
    if line == "":
        break
    line = line.replace("\n", "")
    
    result = translate(line)
    print(line)
    print(f">",result)
    time.sleep(1)

# result = translate("hi")
# print(result)

f.close()