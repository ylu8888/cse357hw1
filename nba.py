# main.py
import numpy as np

def main():
    """
    Main function that acts as the entry point of the program.
    """

    prob_func()

def prob_func():
    N = 10000000
    home_win = 0.75
    away_win = 0.25
    mia_wins = 0
    final_res = 0

    for i in range(N):
        game1 = np.random.binomial(1, away_win) 
        game2 = np.random.binomial(1, away_win)
        game3 = np.random.binomial(1, home_win)
        game4 = np.random.binomial(1, home_win) 
        game5 = np.random.binomial(1, away_win)
        game6 = np.random.binomial(1, home_win)
        game7 = np.random.binomial(1, away_win)  
        
        if(game1 + game2 + game3 == 3): #if mia goes up 3-0
            mia_wins += 1
            
            if(game4 + game5 + game6 == 0):  #if MIA loses next 3
                if(game7 == 1):              #if MIA wins game 7
                    final_res += 1           

    #final_res is MIA wins 4-3, GIVEN that they went 3-0
    print(f"For N = {N}, the simulated value for part (e) is {final_res / mia_wins}") 

if __name__ == "__main__":
    main()
