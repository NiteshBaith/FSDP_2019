"""
The pseudo random generators of this module should not be used for security purposes
Use os.random() or SystemRandom if you require a cryptographically secure pseudo-random number generators
The random() function can be used to build ciustomised random number generators. 

random() and uniform() are both uniform distributions
import random

print(help(random.random))

# Display 10 random numbers from interval [0,1)
for in in range(10):
	print(random.random())

# Generate random numbers from interval [3,7)
def my_random():
	# Random, scale, shift, return...
	return 4*random.random() + 3
for in in range(10):
	print(my_random)

# Alternative
print(help(random.runiform))

for in in range(10):
	print(random.uniform(3,7))


# Display 10 random numbers from interval [0,1) Normally distributed
for in in range(10):
	print(random.normalvariate(0,1))  # mean is 0 and standard deviation 1
	


# Simulate the dice, random number between 1 and 6
randint(min,max)

for in in range(20):
	print(random.randint(1,6))   
	


# Random element from a list
# Rock Paper and Scissor
outcomes = ["rock","paper","scissors"]
for in in range(20):
	print(random.choice(outcomes))  
	



""" 



# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""


"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""


"""
Challenge 6
    Print the number of tries left 
"""


"""
Challenge 7
    Lets give user the option to play again
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""




