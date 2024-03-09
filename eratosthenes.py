import numpy as np
import argparse
import time

def main(lowerbound, n_value):
    n = n_value
    p = 2
    sieve = np.array([[i, True] for i in range(2, 1+n)])
        
    start_time = time.time()

    #for all numbers 2->n
        #choose smallest prime, set to p
        #mark all multiples of p as nonprime
    for potential_nonprime in sieve:
        if potential_nonprime[1] == True:
            p = potential_nonprime[0]
            for i in range(2*p-2, n-1, p):
                sieve[i][1] = False
    
    print(f"Time taken to calculate (results imprecise): {time.time()-start_time}")
    
    for prime_val_index in range(len(sieve)):
        if(prime_val_index > lowerbound) and (sieve[prime_val_index][1] == True):
            print(sieve[prime_val_index][0])
    
    return 1

def parse_arguments():
    #set command line arguments for the program
    parser = argparse.ArgumentParser(description="arg parser for eratosthenes.py -> Provides user with options of what primes to display.")
    parser.add_argument("-lowerbound", type=int, default = 0, help="The lower bound for the displayed primes. Defaults to 0.")
    parser.add_argument("-n", type=int, default = 100, help="Display the prime numbers up to provided value n. Defaults to 100.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    lowerbound = args.lowerbound
    n_val = args.n
    main(lowerbound, n_val)
