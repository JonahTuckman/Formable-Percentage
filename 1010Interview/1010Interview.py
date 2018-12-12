#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:15:18 2018

@author: JonahTuckman
"""

""" 

Language: Python 3
inputs:  String S -> any string of characters, numbers or symbols to be used 
         String name -> name of a text file
         
Program will determine % of words within file represented by F that can be formed
using the letters in S. 

No re-using of letters in input string  

Non-Alphanumberic characters: If they are included in the input, they will be 
attatched to the words alongside them. 
Thus a period, question mark, etc. is attatched to the end of the word prior,
a hyphen would conjoin the two words it is attatched to.
For all examples, the symbol must be included in the input string to be counted as Formable.
The document is split by space between words, not symbols.    

"""

def percentageCalculator(S, name):        
  
   with open(name, "r") as data:
    F = data.readline() # reading the file
    F = F.split(" ") # splitting the file into a list of words
    
    total = len(F)
    wrong = 0
    
    for word in F:
        originalWord = list(S) # So that all words see the same input string
        for i in range(len(word)): 
            if word[i] in originalWord: # if character being checking is in input string
                 originalWord.remove(word[i]) # remove from input string to check for duplicates 
            else:
                wrong += 1 # count wrong and use to find right
                break
       
    right = total - wrong
    percentage = (right/total) * 100
    
    print("{}% Formable".format(percentage))
  

# Testing 
      
exampleInput = "abcdefghijklmnopqrstuvwxyz"
s2 = "a"
lettersAndNumbers = "abcdefghijklmnopqrstuvwxyz0123456789."
lettersNumbersAndSymbols = "abcdefghijklmnopqrstuvwxyz0123456789./,-?!@"

percentageCalculator(exampleInput, "exampleInput.txt") # Gives 33.3333% accuracy -> correct
percentageCalculator(exampleInput,"75Percent.txt") # Gives 75% accuracy -> correct
percentageCalculator(s2, "75Percent.txt") # gives 0% accuracy -> correct
percentageCalculator(lettersAndNumbers, "lettersAndNumbers.txt") #Gives 53.8% -> Correct
percentageCalculator(lettersNumbersAndSymbols, "nonAlphanumeric.txt")
