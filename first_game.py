"""用python设计第一个游戏"""

import random
answer = random.randint(1, 10)

count = 3
while count > 0:

    temp = input("不妨猜一下我现在心里想的是哪个数字：")
    guess = int (temp)

    if guess == answer:
        print("你是我心里的蛔虫嘛？！")
        print("哼，猜中了也没奖励！")
        break
    else:
        if guess < answer:
            print("太小咯~")
        else:
            print("太大咯~")
    count = count - 1


print("游戏结束，不玩啦！")
