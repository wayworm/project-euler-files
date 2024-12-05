# By listing the first six prime numbers: 2,3,5,7,11,13, and , we can see that the 
# 6th prime is 13.

# What is the 10001st prime?

#Aprroach: sieve of [Greek Name]
import numpy as np

import time

## going to endval / 2 is good for funding factors, not important for this problem
def sieve_halfway(list, endval):
    for i in range(2, round(endval / 2)):
        list.append(i)
        for j in range(2,round(i/2)):
            if i % j == 0:
                list.remove(i)


#This gives a list of every prime up to the endval, but I want nth prime...
def sieve(list, endval):
    for i in range(2, round(endval)):
        list.append(i)
        for j in range(2,round(i/2)):
            if i % j == 0:
                try:
                    list.remove(i)
                except:
                    pass
        if i % 50 == 0 :
            print("at",i)


#This gives a list of all primes up to the nth prime 
def list_n_primes(list, n):
    """
    n : number of primes
    """
    i = 2
    j = 2
    while len(list) < n:
        i += 1
        list.append(i)
        for j in range(2,round(i/2)):
            if i % j == 0:
                try:
                    list.remove(i)
                except:
                    pass
        if i % 2000 == 0 :
            length = len(primes)
            print(f"Checked",i,"numbers. At {} th prime.".format(length))


# new approach, hopefully faster. I want to generate a list of all integers up to some value, then sieve on them.
# This didn't work, I didnt plan well enough and made lots of mistakes. Unfinished.

def big_sieve(val):
    vals = np.arange(2, val,1)

    for j in range(3, round(val/2)):
        print("Loop",j)
        for i in range(0,len(vals)):
            try:
                if vals[i] % j == 0:
                    print("deleted",vals[i])
                    vals = np.delete(vals,i)
            except:
                pass

    print(vals)



#Thinking about how to make this more efficient...
def list_n_primes(list, n):
    """
    n : number of primes
    """
    i = 2
    factors = 2
    while len(list) < n:
        i += 1
        #timing
        if i == 4:
            tick = time.time()

        if len(list) + 3 > n:
            tock = time.time()


        list.append(i)
        for factors in range(2,round(i/2)):
            if i % factors == 0:
                try:
                    list.remove(i)
                except:
                    pass
        if i % 2000 == 0 :
            length = len(primes)
            print(f"Checked",i,"numbers. At {} th prime.".format(length))



        
    return list, tock, tick

# realised I could make the program faster with one break haha, not checking every factor, every time
def list_n_primes_time_improve(list, n):
    """
    n : number of primes
    """
    i = 2
    factors = 2
    while len(list) < n:
        i += 1
        #timing
        if i == 4:
            tick = time.time()

        if len(list) + 3 > n:
            tock = time.time()


        list.append(i)
        for factors in range(2,round(i/2)):
            if i % factors == 0:
                try:
                    list.remove(i)
                    break
                except:
                    pass
        if i % 2000 == 0 :
            length = len(primes)
            print(f"Checked",i,"numbers. At {} th prime.".format(length))



        
    return list, tock, tick






#This should be my current best solution
def best_primer(list, n):
    """
    n : number of primes
    """
    i = 2
    factors = 2
    while len(list) < n:
        i += 1

        list.append(i)
        for factors in range(2,round(i/2)):
            if i % factors == 0:
                try:
                    list.remove(i)
                    break
                except:
                    pass
        if i % 2000 == 0 :
            length = len(primes)
            print(f"Checked",i,"numbers. At {} th prime.".format(length))

    return list





primes = []

myprimes = best_primer(primes,10003)

print(myprimes[9999:10004]) # I think we want index 10002, item 3


f = open("primes.txt", "a")
f.write(myprimes)
f.close()
