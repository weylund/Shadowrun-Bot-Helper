import random
import numbers
#regular expressions
#import re
#may be of use for sorting array
#import heapq


global openroll


def rolld6():
  die = random.randint(1,6) 
  roll = die
  while die==6:
    die = random.randint(1,6) 
    roll += die
  return roll
    
def processRolls ():
  global sucesses
  global actualdie
  actualdie = []
  sucesses = 0
  
  for d in range(int(rolls)):
    thisRoll = rolld6()
    actualdie.append(thisRoll)
    if thisRoll >= int(target):
      sucesses = sucesses+1

def splitMessage (message):
  
  #remove the roll instruction from the message and move parameters into list
  trimmedMessage = message[6:]
  splitList = trimmedMessage.split (',')
  splitList = list(map(str.strip, splitList))
  global rolls
  global target
  global reason 

  if len(splitList) == 3:
    #messsage contains dice, target and reason
    rolls = splitList[0]
    target = splitList[1]
    reason = splitList[2]
  elif len(splitList)== 1:
    #message only has dince so a straigh open roll
    rolls = splitList[0]
    target = 0
    reason = ""
  elif len(splitList)==2:
    #message has dice and target or reason
    rolls = splitList[0]
    
    try:
      target = int(splitList[1])
      reason = ""
    except:
      target = 0 
      reason = splitList[1]

def composeResults():
  global resultText
  
  actualdie.sort()

  resultText = "Roll Chummer! " + rolls + "d6 ("
  for d in actualdie:
    resultText+= str(d) + ", "

  #trim last comma
  resultText = resultText[:-2]
  resultText+= ")\n"

  if len(reason) > 1:
    resultText+="Reason: " + reason + "\n"

  if int(target) > 0:
    resultText += str(sucesses) + " sucesses at target: " + str(target) + "\n"
  else:
    resultText += "Best Result: " + str(max(actualdie)) + "\n"

 
def rollChummer(message):
  #text = "Roll 4 6 summon"
  splitMessage(message)
  processRolls()
  composeResults()

  return resultText