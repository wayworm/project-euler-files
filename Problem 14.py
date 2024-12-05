
#Problem 14
#Longest Collatz Sequence

#The following iterative sequence is defined for the set of positive integers:
# n - > n/2  for even n
# n = 3n +1  for odd n

#e.g. 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

#Which starting number, under one million, produces the longest chain?
###Answer should be: 837799 ( I got that)




# I took a long time trying to do this recursively, since I thought it would be cool,
# but the iterative approach was faster and caused me less headache and is how I got the right answer.
# Do what works.

#thoughts

# Use the function I made to calculate the collatz number for each number < 1 million
# sotre the number and it's collatz number
# Find the largest collatz number
# print the number that made that chain

#I've read that Memoization  would make this a lot more efficient. One day...

def collatz_even(n):

    "maps n -> n/2 for even n"

    return int(n/2)


def collatz_odd(n):

    "maps n -> 3*n + 1 for even n"

    return int(3*n + 1)

l = 1

#This work(ed) at one point. I don't like that I had to use a global variable.
def collatz_recursive(n):
        global l

        if n == 1:
                return l        
        elif n % 2 == 0:
            l += 1
            collatz_recursive(collatz_even(n))
                
        else:
              l += 1
              collatz_recursive(collatz_odd(n))

        return l


#This is the way for now. works well.
def collatz_not_recursive(n):
      #flag
      h = 0

      # to include starting value in chain
      l = 1

      #Collatz logic
      while h == 0:

            if n == 1:
                  h = 1
            elif n % 2 == 0:
                  l += 1
                  n = collatz_even(n)
            else:
              l += 1
              n = collatz_odd(n)
      return l


current_longest = 0

#up to end
end  = 1000000

#evalutating
for i in range(1, end):
      n = i
      l = collatz_not_recursive(n)

      if l > current_longest:
            current_longest = l
            best_n = n

      if i % 50000 == 0:
            print("at",i)

print(best_n, "chain of", current_longest)





###

#Stole off of the internet https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
#Only used to check if my code was working.
# def printCollatz(n):
	
# 	# We simply follow steps
# 	# while we do not reach 1
# 	while n != 1:
# 		print(n, end = ' ')

# 		# If n is odd 
# 		if n & 1:
# 			n = 3 * n + 1

# 		# If even 
# 		else:
# 			n = n // 2

# 	# Print 1 at the end 
# 	print(n)


# This code is contributed 
# by vaibhav29498


