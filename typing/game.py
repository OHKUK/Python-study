import time

def play_type_game(path):
# 텍스트 파일의 경로를 입력받음
# 타수를 화면에 출력
    with open(path, "r", encoding="utf-8") as f:
        start_time = time.time()
        string_count = 0
        
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.strip()
            if line != "":
                # string_count = string_count + len(line)
                string_count += len(line)
                
                while True:
                    print(line)
                    user = input()
                    if line == user:
                        break
                    else:
                        print("다시입력")
                        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"타수:{int(string_count / elapsed_time * 60)}/분")

# play_type_game("data/별헤는밤.txt")