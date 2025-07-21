name_ = input('Hello, what is your name? ') # input ชื่อผู้เล่น
numstick = int(input(f'Hi {name_}, how many sticks do you want? ')) # input จำนวนไม้
count_ = 0 # สร้างตัวแปรนับจำนวนครั้งที่ผู้เล่นหยิบไม้เริ่มจาก 0

while numstick > 0: # สร้าง while loop จะหลุดก็ต่อเมื่อจำนวนไม้น้อยกว่า 0
    num_ = int(input(f'{name_}, how many sticks do you will take(1 or 2) : ')) # input จำนวนไม้ที่จะหยิบ
    count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
    if num_ == 1: # สร้าง if ถ้าหยิบไม้ 1 แท่ง
        numstick -= 1 # ลบจำนวนไม้ 1 แท่ง
        print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
    elif num_ == 2: # สร้าง elif ถ้าหยิบไม้ 2 แท่ง
        if numstick < 2: # แล้วถ้าจำนวนไม้ในกองน้อยกว่า 2 แท่ง
            print('There are not enough sticks in the pile to take 2!') # print หยิบไม่ได้
            continue # กลับ loop ใหม่
        else: # ถ้าจำนวนไม้ในกองมากกว่า 2 แท่ง
            numstick -= 2 # ลบจำนวนไม้ 2 แท่ง
            print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
    elif num_ > 2: # ถ้าหยิบไม้มากกว่า 2 แท่ง
        print('No you cannot take more than 2 sticks!') # print หยิบไม่ได้
    else: # ถ้าหยิบไม้ไม่ถึง 1 แท่ง
        print('No you cannot take less than 1 stick!') # print หยิบไม่ได้
print(f'OK. There is no stick left in the pile. You spent {count_} times.') # เมื่อจบเกม print จำนวนครั้งที่ผู้เล่นหยิบไม้
