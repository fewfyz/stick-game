import random as rd  # import library random เพื่อสุ่มตัวเลข

name_ = input('Hello, what is your name? ')  # input ชื่อผู้เล่น
numstick = int(input(f'Hi {name_}, how many sticks do you want? '))  # input จำนวนไม้
count_ = 0  # สร้างตัวแปรนับจำนวนครั้งที่ผู้เล่นหยิบไม้เริ่มจาก 0

User_turn = True  # สร้างตัวแปรเพื่อเช็คว่าเป็นตาของผู้เล่นหรือ AI

while numstick > 0:  # loop จะหลุดเมื่อไม้หมด
    if User_turn:  # ตาของผู้เล่น
        num_ = int(input(f'{name_}, how many sticks do you want to take (1 to 5)? : '))
        if num_ == 1:
            if numstick >= 1:
                numstick -= 1
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print('Not enough sticks to take 1!')
        elif num_ == 2:
            if numstick >= 2:
                numstick -= 2
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print('Not enough sticks to take 2!')
        elif num_ == 3:
            if numstick >= 3:
                numstick -= 3
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print('Not enough sticks to take 3!')
        elif num_ == 4:
            if numstick >= 4:
                numstick -= 4
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print('Not enough sticks to take 4!')
        elif num_ == 5:
            if numstick >= 5:
                numstick -= 5
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print('Not enough sticks to take 5!')

        else:
            print('You can only take 1 to 5 sticks!')

        if numstick == 0:
            print("You took the last stick. You lose!")
            break

    else:  # ตาของ AI
        print("\nAI's turn...")

        # ตำแหน่งที่ใครได้เริ่มเทิร์น จะมีโอกาสแพ้ [1, 7, 13, ...]
        losing_positions = [x for x in range(1, numstick + 1, 6)]

        # กำหนดเงื่อนไขให้ AI ฉลาด
        if (numstick - 5) in losing_positions and numstick >= 5:
            Ai_pick = 5
        elif (numstick - 4) in losing_positions and numstick >= 4:
            Ai_pick = 4
        elif (numstick - 3) in losing_positions and numstick >= 3:
            Ai_pick = 3
        elif (numstick - 2) in losing_positions and numstick >= 2:
            Ai_pick = 2
        elif (numstick - 1) in losing_positions and numstick >= 1:
            Ai_pick = 1
        else:
            Ai_pick = 1 if numstick == 1 else rd.randint(1, min(5, numstick))

        print(f'AI will take {Ai_pick} stick(s).')

        numstick -= Ai_pick
        count_ += 1
        print(f'There are {numstick} sticks in the pile.')

        if numstick == 0:
            print("AI took the last stick. You WIN!")
            break
        else:
            User_turn = True

print(f'OK. There is no stick left in the pile. Total turns taken: {count_} times.')
