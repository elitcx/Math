import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        sum_of_dice = first + second
        return sum_of_dice
        
list = []
times_to_do = 10000
for i in range(times_to_do):
    dice1 = Dice()
    result = dice1.roll()
    list.append(result)
        
results = []
      
for x in range(2,13):
    x_count = 0
    for y in list:
        if y == x:
            x_count += 1
    results.append(x_count)

two_prob = 0
three_prob = 0
four_prob = 0
five_prob = 0
six_prob = 0
seven_prob = 0
eight_prob = 0
nine_prob = 0
ten_prob = 0
eleven_prob = 0
twelve_prob = 0

probabilities = [two_prob, three_prob, four_prob, five_prob, six_prob, seven_prob, eight_prob, nine_prob, ten_prob, eleven_prob, twelve_prob]
strprob = ['2', '3','4','5', '6', '7', '8','9','10','11','12']

for i in range(len(probabilities)):
    probabilities[i] = round(results[i] / 10000 * 100, 2)
    
two_prob, three_prob, four_prob, five_prob, six_prob, seven_prob, eight_prob, nine_prob, ten_prob, eleven_prob, twelve_prob = probabilities

print(probabilities)