import random
import matplotlib.pyplot as plt

def roll():
    return random.randint(1,6)

coins = [10, 12, 15]

def play(coins):
    pos = 0
    while pos < max(coins):
        pos += roll()
        if pos in coins:
            return 1, pos
    return 0, pos            
        
def sim(coins,num):
    win = [0] * num
    pos = [0] * num
    for i in range(num):
        win[i], pos[i] = play(coins)
    winPercentage = float(sum(win)) / num
    return winPercentage

end = 25
coin = [0] * end
for j in range(end):
    coin[j] = sim([6, 5, j],1000)

plt.plot(coin,'bo')
plt.xlabel('Postion')
plt.ylabel('Probability')
plt.show()





