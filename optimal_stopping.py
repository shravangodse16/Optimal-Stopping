import numpy as np
import matplotlib.pyplot as plt

def choose_or_miss(ranks, f):
    """Returns 1 if we get the best candidate in the population by first interviewing a sample set (fraction f)
    and then choosing the next marginally better candidate than the sample. Returns 0 otherwise"""
    
    N = len(ranks)
    best_candidate = np.argmax(ranks) # Location of the best candidate
    sample = int(N*f) # Sample set (# of people we'll interview to select baseline)
    
    #If only 1st candidate in sample set,
    if sample == 0:
        if best_candidate == sample + 1:
            return 1
        elif best_candidate == sample:
            return 0
        elif  np.max(ranks[1:best_candidate]) > ranks[0]:
            return 1
        else:
            return 0

    best_so_far = np.max(ranks[:sample])

    #Unfortunately, the best candidate came in the sample set
    if sample >= best_candidate:
        return 0

    #If the next marginally best cadidate is not the best one in the population
    elif np.max(ranks[sample:best_candidate]) > best_so_far:
        return 0

    #Otherwise, we'll surely choose the best with our strategy
    else:
        return 1

def main():
    N = np.linspace(10, 50, 41, endpoint=True, dtype=int) # Number of applicants 
    f = [0.2, 0.3, 0.4, 0.5] # First fraction of candidates to be interviewed to create a base line
    
    num_iterations = 100000 # Number of iterations to get get probability, can increase if required

    P_random = np.zeros(len(N))
    P_optimal = np.zeros(len(N))
    P_fractions = np.zeros((len(f), len(N)))
    for i, n in enumerate(N):
        choose_optimal = 0
        choose_random = 0
        choose_fraction = np.zeros(len(f))
        for j in range(num_iterations):
            ranks = np.linspace(0, n-1, n, endpoint=True, dtype=int) #Ranking of candidates
            #Randomly place the candidates so we don't when we will get the best one
            np.random.shuffle(ranks)
            
            #--------------Optimal Strategy------------------#
            #Interview N/e candidates and then choose the next marginally best candidate than the sample
            if choose_or_miss(ranks, 1/np.e):
                choose_optimal += 1
            
            #--------------Stopping randomly-----------------#
            if choose_or_miss(ranks, np.random.random()):
                choose_random += 1
            
            #---------For comparison, interviewing the first fraction 'f' candidates and then selecting best----------#
            for k, f_ in enumerate(f):
                if choose_or_miss(ranks, f_):
                    choose_fraction[k] += 1
        
        P_optimal[i] = choose_optimal/num_iterations
        P_random[i] = choose_random/num_iterations
        P_fractions[:, i] = choose_fraction/num_iterations
    
    # Plot results
    plt.figure(figsize=(10,8))
    plt.plot(N, P_random, label='Randomly Stopping')
    plt.plot(N, P_optimal, label='Stopping after 1/e')

    for i, p_f in enumerate(P_fractions):
        plt.plot(N, p_f, label=f'Stopping after {f[i]}')

    plt.xlabel('Number of Candidates')
    plt.ylabel('Probability of choosing the best')
    plt.legend()
    plt.savefig('OptimalStopping.PNG', dpi=300)
    plt.show()
if __name__ == '__main__':
    main()