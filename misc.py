#PA 4

import re

"Miscellaneous functions to practice Python"

class Failure(Exception):
    """Failure exception"""
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

# Problem 1

# data type functions

def closest_to(l,v):
  l = sorted(l)
  closestNum = None
  closestSoFarLeft = None
  closestToRight = None
  for i in l:
    # a number equal to v, simply return it 
    if i == v:
      return v     
    # keep track of closest number that is less than target
    elif i < v:
      closestSoFarLeft = i
    # just get first num that is greater than target
    else:
      closestToRight = i
      break
  # Check which value to return
  if closestToRight == None:
    return closestSoFarLeft
  # check which number is closest
  else: 
    if v - closestSoFarLeft < closestToRight - v:
      closestNum = closestSoFarLeft
    elif v - closestSoFarLeft > closestToRight - v:
      closestNum = closestToRight
    else:
      closestNum = closestSoFarLeft
  return closestNum

    

def make_dict(keys,values):
  dictionary = {}
  for key, value in zip(keys,values):
    dictionary[key] = value 
  return dictionary 
   
   
# file IO functions
def word_count(fn):
  wordDict = {}
  f = open(fn,"read")
  lines = list(f.readlines)
  for l in lines:
    wordDict[l.lower()]+=1
        
  return wordDict







