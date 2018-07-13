# This is a game designed as a case study at the end of Course 2
# of Data Camp's Career Track Python Data Scientist
# https://www.datacamp.com/tracks/data-scientist-with-python
# Game Premise: You and a friend are playing a game in the Empire State Building
# You bet a friend that after 100 dice throws you will go up 60 steps
# You throw a dice, its number indicates, whether you go up or down the stairs
# Throw a 1 or 2 and you do down 1 step
# Throw a 3 - 5 and go up 1 step
# Throw a 6 and you get to throw again, that number gives you the number of
# steps you get to up
# There is also a 0.1% chance you fall down the steps, back to step 0
# Task: Design a Script to simulate the game and the results
# Task 2: What are the chance you will do 60 steps or higher and win the game?

# Script

# Import numpy and set seed
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# setting a seed means the randomn numbers will be the same every time the
# script is run, meaning you get consistency in results, otherwise for random
# results every time set as follows np.random.seed()


# now we being to simulate the distribution or random walks, i.e what is
# the most likely steps I will take, will it be 30,40, 50 etc.
# when random_walk is iterated a number of times
all_walks = []

# Simulate random walk 500 times
for i in range(500) :

# Initialize random_walk

    random_walk = [0]
# we set randomn walk at step 0

# Complete the ___
    for x in range(100):

        step = random_walk[-1]
        # Set step: last element in random_walk

        # Roll the dice
        dice = np.random.randint(1,7)

        # We use randint, to give whole numbers between 1 and 6 (the numbers of the dice)

        # Determine next step
        if dice <= 2:
            step = max(0,step - 1)
        #insert max function to ensure, steps cannot go below 0
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

         # Implement clumsiness
        if np.random.rand(0,1) <= 0.001 :
            step = 0

# append next_step to random_walk
        random_walk.append(step)

# append random_walk to all_walks

    all_walks.append(random_walk)

# Print all_walks

# print(all_walks) - appended , originally we only had to print 10 values, and
# now its 250, so we save ourselves the time

# Convert all_walks to Numpy array: np_aw

np_aw = np.array(all_walks)

# Plot np_aw and show

#plt.plot(np_aw)
#plt.show()

# Clear the figure - When we print it, the relationship is unclear, so we clear
# and transpose the 2-D array, essentially a 2-D Matrix

#plt.clf

# Create and plot np_aw_t

np_aw_t = np.transpose(np.array(all_walks))

#plt.plot(np_aw_t)
#plt.show()

# Though a pyplot (appended above) is all well and good, we are really only
# interested in the last row i.e. the result of each randomn walk
# which we can now put into a histogram to find the most likely number of
# steps over 500 iterations of our random_walk

# Select last row from np_aw_t: ends

ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot

plt.hist(ends)
plt.show()

# finally we calculate the chance that we will reach 60 steps or higher
# and win the game

chance_to_win = np.mean(ends >= 60)
print(chance_to_win)

# answer = 0.84 or 84%, with DataCamp it came out to 0.784
# a pretty good chance of winning
