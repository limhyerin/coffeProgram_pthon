# 커피자판기 프로그램

print("              *")
print("             ***")
print("           ******")
print("====================")
print("=                  =")
print(" =                =")
print("  =     COFFEE   =")
print("   =            =")
print("    =          =")
print("     ==========")
print()
print()
print("OO커피 자판기 메뉴판")
print("a. 아메리카노 1800원")
print("b. 카페라떼 2700원")
print("c. 핫초코 2300원")
print("====================")
print()
while True:
    user_input = input("커피종류를 선택하세요. 커피 선택>> ")
    num = int(input("몇잔?"))
    sum_m = 0
    if user_input == "a":
        sum_m = num*1800
    elif user_input == "b":
        sum_m = num*2700
    elif user_input == "c":
        sum_m = num*2300
    else:
        print("잘못된 입력입니다")
    print("====================")
    print("총 금액 {}원입니다.".format(sum_m))
    money = int(input("돈을 투입해주세요>> "))
    print()
    re = money - sum_m
    if money > sum_m:
        print("{}원을 받았습니다. 거스름돈은 {}원입니다".format(money,re))
        print("서비스를 종료합니다")
        break
    else:
        lack = sum_m - money
        print("총금액 {}원, 지급하신 금액 {}원으로 {}원이 부족합니다".format(sum_m, money, lack))
        print("구매를 원하시면 다시 서비스를 이용해주세요. 서비스를 종료합니다")
        break
