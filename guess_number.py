# 46/47 猜數字遊戲

import random

start = input ('Please let me know the minimum of number you want to guess: ')
end = input ('Please let me know the maximum of number you want to guess: ')


r = random.randint (int(start), int(end))

count = 0
while True:
    count += 1 #count = count + 1
    num = input ('Please enter a number: ')
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
