"""
Functions for ActivityLogger
Luke Fitzpatrick 2014
"""
import os.path
from datetime import *
ACTIVITYFILENAME = "activities.txt"
    
    

def loadActivities():
    """
    Loads and returns a list of all activities in the activities.txt file.
    """
    try:
        f = open(ACTIVITYFILENAME, 'r')
        lines = []
        for line in f:
            lines.append(line.strip(' \t\n\r'))
        return lines
    except:
        print "Couldn't open " + ACTIVITYFILENAME + "."
   
def validateActivityName(name):
    """
    Takes an activity name and verifies that it exists in the activities file.
    Returns true/false.
    """
    #all of the names in the file are lowercase, the names are not case sensitive.
    if name.lower() in loadActivities():
        return True
    else:
        return False
    
def validateTimestamp(timeStamp):
    """
    Takes a user provided timeStamp and verifies that it follows the correct format.
    Returns true/false.
    Valid timestamp formatting:
        [TIME1] to [TIME2]
        TIME: integer number of hours before current time.
        [TIME2] <= [TIME1]
    """
    words = timeStamp.split()
  
    try:
        if(words[0].isdigit() and words[1] == "to" and words[2].isdigit()):
            if(int(words[2]) <= int(words[0])):
                return True
    except:
        pass
    
    return False
    
def validateComment(comment):
    """
    Takes a user provided comment and verifies it is valid.
    Returns true/false.
    """
    if "\n" in comment or "," in comment:
        return False
    return True
    
def convertInputToData(timeStamp, comment):
    """
    Takes a correct user timeStamp and comment and converts it to the data folder format.
    Returns string with the correct data folder formatted data.
    """
    words = timeStamp.split()
    timestamp1 = datetime.now() - timedelta(minutes = int(words[0]))
    timestamp2 = datetime.now() - timedelta(minutes = int(words[2]))
    
    data = str(timestamp1) + "," + str(timestamp2) + "," + comment
    return data

def writeDataToFile(activityName, data):
    """
    Writes the provided data to the file of the activityName.
    """
    fileName = "data/" + activityName + ".txt"
    with open(fileName, 'a') as file:
        file.write(data)
        file.write("\n")

def getValidatedInput(message, validationFunction):
    """
    Prints message, gets input and continues to do this until
    validationFunction returns true.
    """
    valid = False
    while (not valid):
        value = raw_input(message)
        valid = validationFunction(value)
    
    return value
