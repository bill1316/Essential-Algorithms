import random
'''
Getting Fairness from Biased Sources:

Loop for 10 times
Flip the biased coin twice.
If the result is {Heads, Tails}, return Heads.
If the result is {Tails, Heads}, return Tails.
If the result is something else, start over.

Hint: Biased coin can be implemented as follows in Python.
'''

def BiasedCoin():
    number = random.randint(1,4)
    if number == 3:
         return "tail"
    else:
         return "head"

def flipCoin(BiasedCoin):
      flip1, flip2 = BiasedCoin(), BiasedCoin()
      if flip1 == "head" and flip2 == "tail":
          return "head"
      elif flip1 == "tail" and flip2 == "head":
          return "tail"
      else:
          return flipCoin(BiasedCoin)


result= []
for i in range(10):
    i = flipCoin(BiasedCoin)
    result.append(i)


print flipCoin(BiasedCoin)
print result
