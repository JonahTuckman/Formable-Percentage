#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:15:18 2018

@author: JonahTuckman
"""

""" 

Language: Python 3
inputs:  String S -> any string 
         String F -> name of a text file
         
Program will determine % of words within file represented by F that can be formed
using the letters in S. 

No resusing of letters         

"""

def percentageCalculator(S, name):        
  
   with open(name, "r") as data:
    F = data.readline()
    F = F.split(" ")
    
    total = 0
    right = 0
    wrong = 0
    for word in F:
        total += 1
        originalWord = list(S)
        for i in range(len(word)):
            if word[i] in originalWord:
                 originalWord.remove(word[i])
            else:
                wrong += 1
                break
       
    right = total - wrong
    percentage = (right/total) * 100
    
    print("{}% Formable".format(percentage))
  

# Testing 
      
exampleInput = "abcdefghijklmnopqrstuvwxyz"
s2 = "a"
lettersAndNumbers = "abcdefghijklmnopqrstuvwxyz0123456789."

percentageCalculator(exampleInput, "exampleInput.txt") # Gives 33.3333% accuracy -> correct
percentageCalculator(exampleInput,"75Percent.txt") # Gives 75% accuracy -> correct
percentageCalculator(s2, "75Percent.txt") # gives 0% accuracy -> correct
percentageCalculator(lettersAndNumbers, "lettersAndNumbers.txt") #Gives 53.8% -> Correct
