name_ = input('Hello, what is your name? ')
numstick = int(input(f'Hi {name_}, how many sticks do you want? '))
count_ = 0

while numstick > 0 :
    num_ = int(input(f'{name_}, how many sticks do you will take(1 or 2) : '))
    count_ += 1
    if num_ == 1 :
        numstick -= 1
        print(f'There are {numstick} sticks in the pile.')
    elif num_ == 2 :
        if numstick < 2 :
            print('There are not enough sticks in the pile to take 2!')
            continue
        else:   
            numstick -= 2
            print(f'There are {numstick} sticks in the pile.')
    elif num_ > 2 :
        print('No you cannot take more than 2 sticks!')
    else :
        print('No you cannot take less than 1 stick!')

print(f'OK. There is no stick left in the pile. You spent {count_} times.')

