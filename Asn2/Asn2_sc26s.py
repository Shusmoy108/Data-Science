import numpy as np
import time
import random
from matplotlib import pyplot as plt

def plotgraph(max_sum,prob, dice_num, trials):
    plt.title(f"Probability with {dice_num} dice over {trials} trials")
    plt.xlabel("Roll")
    plt.ylabel("Probability")
    x = [ i for i in range(max_sum) ]
    plt.plot(x,prob, "ob")
    plt.show()

def dice_game(dice_num,trials):
    start = time.time()
    max_sum=dice_num*6+1;
    num_dice = np.zeros(max_sum, dtype=np.int64)
    for i in range(0,trials):
        total_dice=0
        for j in range(0,dice_num):
            total_dice=total_dice+random.randint(1,6)
        num_dice[total_dice]=num_dice[total_dice]+1
    prob = np.zeros(max_sum)
    for i in range(0,max_sum):
        prob[i]=num_dice[i]/trials
        end = time.time()
    print(f"Your program elapsed time {end - start}s")
    plotgraph(max_sum,prob,dice_num,trials)
    
def main():
    while True:
        #start = time.time()
        input1= input("Enter the number of dice: ")
        
        if(input1=="quit" or input1=="Quit"):
            break
        elif(input1.isdigit()==False):
            print("Enter a digit for number of dice")
            continue
        input2= input("Enter the number of trials: ")
        if(input2=="quit" or input2=="Quit"):
            break
        elif(input2.isdigit()==False):
            print("Enter a digit for number of trials")
            continue
        dice_number= int(input1)
        trial_number= int(input2)
        dice_game(dice_number,trial_number)
        #print(prob)
        #end = time.time()
        #print(f"Your program elapsed time {end - start}s")
        

main()
