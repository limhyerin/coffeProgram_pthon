# 컴퓨터 VS 유저 가위바위보 게임 프로그램

import random
print("*************************")
print("     가위바위보 게임")
print("*************************")
print()

name_input = input("이름을 입력하세요>> ")
print()
print("*************************")
print("S     T     A     R     T")
print("*************************")

while True:
    pc_choice = ["가위", "바위", "보"]
    pc = random.choice(pc_choice)
    user_input = input("가위/바위/보 중 하나를 입력하세요(종료시 \"종료\" 입력) >> ")
    print()
    
    if user_input == "가위" and pc == "가위":
        print("비겼습니다")
    elif user_input =="가위" and pc == "바위":
        print(f"{name_input}님이 가위를 냈고 pc가 바위를 냈으므로 {name_input}님의 패배")
    elif user_input =="가위" and pc == "보":
        print(f"{name_input}님이 가위를 냈고 pc가 보를 냈으므로 {name_input}님의 승리")
    elif user_input == "바위" and pc == "바위":
        print("비겼습니다")
    elif user_input =="바위" and pc == "보":
        print(f"{name_input}님이 바위를 냈고 pc가 보를 냈으므로 {name_input}님의 패배")
    elif user_input =="바위" and pc == "가위":
        print(f"{name_input}님이 바위를 냈고 pc가 가위를 냈으므로 {name_input}님의 승리")
    elif user_input == "보" and pc == "보":
        print("비겼습니다")
    elif user_input =="보" and pc == "가위":
        print(f"{name_input}님이 보를 냈고 pc가 가위를 냈으므로 {name_input}님의 패배")
    elif user_input =="보" and pc == "바위":
        print(f"{name_input}님이 보를 냈고 pc가 바위를 냈으므로 {name_input}님의 승리")
    elif user_input == "종료":
        break
    print()
