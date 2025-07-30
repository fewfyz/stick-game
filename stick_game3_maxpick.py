import random as rd  # import library random เพื่อสุ่มตัวเลข

# รับข้อมูลจากผู้เล่น
name_ = input('Hello, what is your name? ')
numstick = int(input(f'Hi {name_}, how many sticks do you want to play with? '))
max_pick = int(input(f'And what is the maximum number of sticks you can take per turn? '))

count_ = 0  # ตัวแปรนับจำนวนครั้ง
User_turn = True  # เริ่มที่ผู้เล่น

while numstick > 0:
    if User_turn:
        try:
            num_ = int(input(f'{name_}, how many sticks do you want to take (1 to {max_pick})? : '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= num_ <= max_pick:
            if numstick >= num_:
                numstick -= num_
                count_ += 1
                print(f'There are {numstick} sticks in the pile.')
                User_turn = False
            else:
                print(f'Not enough sticks to take {num_}!')
        else:
            print(f'You can only take between 1 and {max_pick} sticks!')

        if numstick == 0:
            print("You took the last stick. You lose!")
            break

    else:
        print("\nAI's turn...")

        # คำนวณตำแหน่งที่ใครได้เริ่มตานั้นจะมีโอกาสแพ้
        losing_positions = [x for x in range(1, numstick + 1, max_pick + 1)]

        # AI หาทางเลือกที่ดีที่สุด
        Ai_pick = None
        for i in range(max_pick, 0, -1):
            if (numstick - i) in losing_positions and numstick >= i:
                Ai_pick = i
                break

        if Ai_pick is None:
            Ai_pick = 1 if numstick == 1 else rd.randint(1, min(max_pick, numstick))

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
