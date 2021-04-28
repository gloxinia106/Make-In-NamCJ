from time import sleep

total_set = input("Juarez Valley Method 세트수: ")

odd_set = int(total_set)
even_set = 1
first_set = 1
last_set = total_set

while(first_set <= int(total_set)):
    print("="*20)
    print(f"{first_set}Set")
    print("\n")
    if(first_set %2 ==1):
        print(f"{odd_set}번 푸쉬업 하세요")
        print("\n")
        input("다 끝나면 enter키를 눌러주세요")
        odd_set -= 1
    else:
        print(f"{even_set}번 푸쉬업 하세요")
        print("\n")
        input("다 끝나면 enter키를 눌러주세요")
        even_set += 1
    print("\n")
    print("Break Time")

    for end_time in range(0,15):
        print(15 - end_time)
        sleep(1)

    first_set += 1

input("끝")
