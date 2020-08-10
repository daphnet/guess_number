# 46/47 猜數字遊戲

import random

r = random.randint (1, 100)

count = 0
while True:
    count += 1 #count = count + 1
    num = input ('Please enter a number between 1 to 100: ')
    num = int(num)
    if num == r:
        print ('Great, you got it!!')
        print ('This is try', count)
        break
    elif num < r:
        print ('Your guess is smaller than the answer.')
    elif num > r:
        print ('Your guess is larger than the answer.')
    print ('This is try', count)
