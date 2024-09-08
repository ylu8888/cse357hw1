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

    probA = 0 #MIA up 3-0
    home_win = 0.75
    away_win = 0.25
    mia_wins = 0
    comeback_wins = 0
    final_res = 0

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
        game4 = np.random.binomial(1, home_win) 
        game5 = np.random.binomial(1, away_win)
        game6 = np.random.binomial(1, home_win)
        game7 = np.random.binomial(1, away_win)  
        
        win_three = game1 + game2 + game3
        if(win_three == 3): #if mia goes up 3-0
            mia_wins += 1

        lose_three = game4 + game5 + game6
        if(lose_three == 0): #if mia loses games 4,5,6
            if(game7 == 1): #if mia wins game 7
                comeback_wins += 1 #P(losing first 3 and winning last) == 0.25 * 0.75 * 0.25 * 0.25 = 0.01172
        
        if(win_three == 3 and lose_three == 0): #if MIA wins 4-3, GIVEN that they went 3-0
            if(game7 == 1):
                final_res += 1

    probA = mia_wins / N #0.25 * 0.25 * 0.75 = 0.047
    #print(f"The probability of MIA going up 3-0 is {probA}") 

    #probability MIA loses games 4-6 then wins game7, 0.25 * 0.75 * 0.25 * 0.25 = 0.0117
    print(f"For N = {N}, the simulated value for part (e) is {comeback_wins / N}")

    #0.25 * 0.25 * 0.75 * 0.25 * 0.75 * 0.25 * 0.25 = 0.00055
    #print(f"The probability MIA wins 4-3, given they were up 3-0 is {final_res / N}") 


if __name__ == "__main__":
    main()
