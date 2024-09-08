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
    probBA = 0 #MIA wins 4-3
    home_win = 0.75
    away_win = 0.25
    mia_wins = 0
    comeback_wins = 0
    res = 0

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

            game4 = np.random.binomial(1, home_win) 
            game5 = np.random.binomial(1, away_win)
            game6 = np.random.binomial(1, home_win)
            game7 = np.random.binomial(1, away_win) 

            if(game4 + game5 + game6 == 0): #if mia loses games 4,5,6
                if(game7 == 1): #if mia wins game 7
                    #P(losing first 3 and winning last) == 0.25 * 0.75 * 0.25 * 0.25 = 0.01172
                    comeback_wins += 1 

    #print(f"The probability of MIA going up 3-0 is {probA}") 
    probA = mia_wins / N   #this is the probability MIA goes up 3-0, 0.25 * 0.25 * 0.75, roughly 0.047

    probBA = comeback_wins / N #this is the probability MIA loses games 4-6 then wins game7, roughly 0.01172

    res = probBA / probA #this is the final solution, the prob MIA wins 4-3, given they were up 3-0

    print(f"The probability MIA wins 4-3, given they were up 3-0 {res}")

    for i in range(N):
        game4 = np.random.binomial(1, home_win) 
        game5 = np.random.binomial(1, away_win)
        game6 = np.random.binomial(1, home_win)
        game7 = np.random.binomial(1, away_win) 

        if(game4 + game5 + game6 == 0): #if mia loses games 4,5,6
                if(game7 == 1): #if mia wins game 7
                    #P(losing first 3 and winning last) == 0.25 * 0.75 * 0.25 * 0.25 = 0.01172
                    comeback_wins += 1 

    res_2e = comeback_wins / N

    print(f"For N = {N}, the simulated value for part (e) is {res_2e}")

if __name__ == "__main__":
    main()
