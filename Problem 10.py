# Find the sum of all the primes below two million. (UNFINISHED)

# ISSUE: MY sieve function is way to slow, It'll take 20 mins or so to get to 2 million...
# But not_prime_sieve() does give the right answer for primes to 100 and primes to 200




#Functions from problem 7

#This should be my current best solution, a copy/paste of one of my functions
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



# WAY TOO SLOW
def not_prime_sieve(endval):
    """Minuses all non-prime values from the sum of integers up to endval"""
    total = int( (endval)*(endval+1)/2  )
    print("total i  hope",total)
    for i in range(2, round(endval)+1):
        for j in range(2,round(i/2)+1):
            if i % j == 0:
                total = total - i
                break
        if i % 50000 == 0 :
            print("at",i)

    return total - 1



primes = []
upto = 2000000

out = not_prime_sieve(upto)

print(out)

f = open("C:\\Users\\Tedder\\Documents\\.Python Project\\Project EulerProbelm 10.txt", "a")
message = "The sum with no primes"+ str(out), "original total:" + str(upto)
strmessage = str(message)
f.write(strmessage)
f.close()
