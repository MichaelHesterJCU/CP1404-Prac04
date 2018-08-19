"""
A program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
"""
import random
def main():
    user_input = int(input("Enter the amount of picks: "))
    for count in range(0,user_input):
        lotto_picks = []
        lotto_picks = random_number_generator(lotto_picks)
        print(*lotto_picks)
        del lotto_picks

def random_number_generator(pick_comparison):           #Generates a random set of 6 numbers with no repeating
    count = 0
    while count in range(0,6):
        random_number = random.randint(1,45)
        if random_number not in pick_comparison:
            pick_comparison.append(random_number)
            count = count + 1
    return pick_comparison

main()