import matplotlib.pyplot as plt
import numpy as np

# You may wish to write some code here

def binomial(n, p) :
  # Your code to generate a binomial random variable goes here
  
nparam, prob = 8, 0.3
noutcomes = 
counts = np.zeros(noutcomes)
for i in range(200) : 
  # Your code to generate multiple binomial variables using the function
  # called binomial above and to count how often each outcome comes
  # up goes here.  
  
  
sample_space = np.zeros(0)
for i in range(noutcomes) : 
  # Your function to convert the count of the number of times each 
  # value for the random variable comes up to the fraction of times
  # each outcome comes up goes here.  You should also set the elements
  # of the list sample_space to the various values in the sample space for this particular random variable so that the plot appears correctly.
  
# These command will plot your histogram
plt.bar( sample_space, counts, width=0.1 )
plt.xlabel("Random variable value")
plt.ylabel("Fraction of occurances")
plt.savefig("myhistogram.png")
