# A number greater than 1 is called a prime number, 
# if it has only two factors, namely 1 and the number itself. 
   
# Public-key cryptography, which relies on the difficulty of factoring large 
# numbers into their prime factors.


"""
Proof by Contradiction

One of the first known proofs is the method of contradiction. 
It is used to calculate prime factors of large numbers. 
Calculating prime factors of small numbers is easy. 
For example, the factors of 17 is 1 and 17, so it is a prime number. 
What about large numbers? Let's look at the proof by contradiction method.

If a number n is not a prime, it can be factored into two factors a and b, 
such that n = a*b. For example, let's say a * b = 100, for various pairs of a and b.

If a = b, then they are equal, we have a*a = 100, or a^2 = 100, or a = 10, the square root of 100. 
If one of the numbers is less than 10, then the other has to be greater to make it to 100. For example, 
take 4 x 25 = 100. 4 is less than 10, the other number has to be greater than 10. 
In other words, if a * b, if one of them goes down, the other number has to get 
bigger to compensate so the product stays at 100. 
Put mathematically, the numbers revolve around the square root of their product. 

Let's test if 101 is prime number. You could start dividing 101 by 2, 3, 5, 7, 
etc, but that is very tedious. A better way is to take the square root of 101, 
which is roughly equal to 10.049875621. So you only need to try the integers up 
through 10, including 10. 8, 9, and 10 are not themselves prime, so you only have 
to test up through 7, which is prime.
​
Because if there's a pair of factors with one of the numbers bigger than 10, 
the other of the pair has to be less than 10. If the smaller one doesn't exist,
there is no matching larger factor of 101. 

Let's now build an algorithm using this method to test any number for primality. 

https://inventwithpython.com/hacking/chapter23.html

"""



import math

def is_prime(n):
  """Determine if a non-negative integer is prime"""
  if n < 2 :
    return False

  # OFF BY ONE Error, solution is to add +1  
  #for i in range (2, int(math.sqrt(n)) + 1 ):
  for i in range (2, int(math.sqrt(n))  +1 ):
    if n % i == 0 :
      return False
  return True


# compile this file from the terminal or command prompt using python prime.py


# list of prime numbers

# is_prime WILL return TRUE  
# 2, 3, 5, 7, 11, 13, 17, 19, 23
  
# is_prime WILL return FALSE  
# 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28

"""
is_prime(1)   # SUCCESS
is_prime(2)   # SUCCESS
is_prime(8)   # FAIL   
is_prime(11)  # SUCCESS
is_prime(25)  # FAIL 
is_prime(28)  # SUCCESS
  
"""

