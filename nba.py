# main.py
import numpy as np

def main():
    """
    Main function that acts as the entry point of the program.
    """
    #print("Welcome to the new Python program!")
    # Your code starts here
    prob_func()

def prob_func():
    N = 10000
    res = 0

    probA = 0 #MIA up 3-0
    probB = 0 #MIA wins 4-3
    home_win = 0.75
    away_win = 0.25
    mia_wins = 0

    #g1 = bos
    #g2 = bos
    #g3 = mia
    #g4 = mia
    #g5 = bos
    #g6 = mia
    #g7 = bos

    for i in range(N):
        game1 = np.random.binomial(1, away_win) 
        game2 = np.random.binomial(1, away_win)
        game3 = np.random.binomial(1, home_win) 
        
        if(game1 + game2 + game3 == 3): #if mia goes up 3-0
            mia_wins += 1

    probA = mia_wins / N   

    print(f"The probability of MIA going up 3-0 is {probA}")
    
    comeback_wins = 0
  
    for i in range(N): 
        game4 = np.random.binomial(1, home_win) 
        game5 = np.random.binomial(1, away_win)
        game6 = np.random.binomial(1, home_win)
        game7 = np.random.binomial(1, away_win) 

        if(game4 + game5 + game6 == 0):
            if(game7 == 1):
                comeback_wins += 1 

    #P(losing first 3 and winning last) == 0.25 * 0.75 * 0.25 * 0.25
    #the expected prob (mia_victory) should be 0.01172
    mia_victory = comeback_wins / N #this is the probability MIA loses 3 then wins 1
    print(f"The REAL probability of MIA losing game 4-6 and winning game 7 is {mia_victory}")

    probB = mia_victory * probA
    
    print(f"The probability of MIA winning 4-3 is {probB}")
    
    #print(f"For N = {N}, the simulated value for part (e) is {mia_wins}")

if __name__ == "__main__":
    main()
