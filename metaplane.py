import os
import csv
import random

VisitedLocations = []

#Remove extranious charcters from string
def CleanString (originalString):
  characters_to_remove = "(),"

  new_string = originalString
  for character in characters_to_remove:
    new_string = new_string.replace(character, "")

  return new_string

#Check if a location has been visited yet
def VisitedLocation (locationID):
  if locationID in VisitedLocations:
    result = True
  else:
    result = False
  return result

#Cycle round the places correctly.
def CheckLocation(locationID):
  if locationID > 7:
    locationID = locationID - 7
  if VisitedLocation (locationID):
    locationID = CheckLocation(locationID+1)
    
  return locationID

def AstralQuest():
  with open('Metaplaces.txt', newline='') as f:
      reader = csv.reader(f)
      data = [tuple(row) for row in reader]
    
  NextLocation = 0
  result = "The Dweller on the Threshold guides your journey:\n"

  while NextLocation != 7:
    NextLocation = CheckLocation((random.randint(2,12) -1))
    VisitedLocations.append(NextLocation)
    result = result + "\n" + str((data[NextLocation]))

  result = CleanString(result)
  VisitedLocations.clear()

  return result