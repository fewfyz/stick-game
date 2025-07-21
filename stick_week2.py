import random as rd # import library random เพื่อสุ่มตัวเลข

name_ = input('Hello, what is your name? ') # input ชื่อผู้เล่น
numstick = int(input(f'Hi {name_}, how many sticks do you want? ')) # input จำนวนไม้
count_ = 0 # สร้างตัวแปรนับจำนวนครั้งที่ผู้เล่นหยิบไม้เริ่มจาก 0

User_turn = True # สร้างตัวแปรเพื่อเช็คว่าเป็นตาของผู้เล่นหรือ AI

while numstick > 0: # สร้าง while loop จะหลุดก็ต่อเมื่อจำนวนไม้น้อยกว่า 0

    if User_turn == True : # ตาของผู้เล่น
        num_ = int(input(f'{name_}, how many sticks do you will take(1 or 2) : ')) # input จำนวนไม้ที่จะหยิบ
        if num_ == 1: # สร้าง if ถ้าหยิบไม้ 1 แท่ง
            if numstick == 1 : # ถ้าจำนวนไม้เหลือ 1 แท่ง
                numstick -= 1 # ลบจำนวนไม้ 1 แท่ง
                count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
                print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
            else :
                numstick -= 1 # ลบจำนวนไม้ 1 แท่ง
                count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
                print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
                User_turn = False # เปลี่ยนเป็นตาของ AI
        elif num_ == 2: # สร้าง elif ถ้าหยิบไม้ 2 แท่ง
            if numstick == 2 : # ถ้าจำนวนไม้เหลือ 2 แท่ง
                numstick -= 2 # ลบจำนวนไม้ 2 แท่ง
                count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
                print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้    
            elif numstick < 2: # แล้วถ้าจำนวนไม้ในกองน้อยกว่า 2 แท่ง
                print('There are not enough sticks in the pile to take 2!') # print หยิบไม่ได้
                continue # กลับ loop ใหม่
            else: # ถ้าจำนวนไม้ในกองมากกว่า 2 แท่ง
                numstick -= 2 # ลบจำนวนไม้ 2 แท่ง
                count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
                print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
                User_turn = False # เปลี่ยนเป็นตาของ AI
        elif num_ > 2: # ถ้าหยิบไม้มากกว่า 2 แท่ง
            print('No you cannot take more than 2 sticks!') # print หยิบไม่ได้
        else: # ถ้าหยิบไม้ไม่ถึง 1 แท่ง
            print('No you cannot take less than 1 stick!') # print หยิบไม่ได้
        
        if numstick == 0: # ถ้าจำนวนไม้เหลือ 0 แท่ง
                print("You took the last stick. You lose!") # print ผู้เล่นแพ้
                break # จบเกมถ้าผู้เล่นหยิบไม้หมด
         
    if User_turn == False : # ตาของ AI
        Ai_pick = rd.randint(1, 2) # สุ่มจำนวนไม้ที่ AI จะหยิบ 1 หรือ 2 แท่ง
        print(f'AI will take {Ai_pick} sticks.') # print จำนวนไม้ที่ AI จะหยิบ
        
        if numstick == 1:
            Ai_pick = 1 # ถ้าจำนวนไม้เหลือ 1 แท่ง AI จะหยิบ 1 แท่ง
            numstick -= 1 # ลบจำนวนไม้ 1 แท่ง
            count_ += 1 # นับจำนวนครั้งที่ AI หยิบไม้เพิ่มไป
            print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
            User_turn = True # เปลี่ยนเป็นตาของผู้เล่น
        elif Ai_pick == 1: # สร้าง if ถ้า AI หยิบไม้ 1 แท่ง
            numstick -= 1 # ลบจำนวนไม้ 1 แท่ง
            count_ += 1 # นับจำนวนครั้งที่ AI หยิบไม้เพิ่มไปทีละ 1 ครั้ง
            print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
            User_turn = True # เปลี่ยนเป็นตาของผู้เล่น
        elif Ai_pick == 2: # สร้าง elif ถ้าหยิบไม้ 2 แท่ง
            if numstick < 2: # แล้วถ้าจำนวนไม้ในกองน้อยกว่า 2 แท่ง
                print('There are not enough sticks in the pile to take 2!') # print หยิบไม่ได้
                continue # กลับ loop ใหม่
            else: # ถ้าจำนวนไม้ในกองมากกว่า 2 แท่ง
                numstick -= 2 # ลบจำนวนไม้ 2 แท่ง
                count_ += 1 # นับจำนวนครั้งที่ผู้เล่นหยิบไม้เพิ่มไปทีละ 1 ครั้ง
                print(f'There are {numstick} sticks in the pile.') # print จำนวนไม้ที่เหลือ
                User_turn = True # เปลี่ยนเป็นตาของผู้เล่น
       
        if numstick == 0: # ถ้าจำนวนไม้เหลือ 0 แท่ง
                print("Ai took the last stick. You WIN!") # print ผู้เล่นชนะ
                break  # จบเกมถ้าผู้เล่นชนะ
                
print(f'OK. There is no stick left in the pile. Total turns taken : {count_} times.') # print จำนวนครั้งที่ผู้เล่นและ AI หยิบไม้รวมกัน
