"""
Functions for ActivityLogger
Luke Fitzpatrick 2014
"""

def loadActivities():
    """
    Loads and returns a list of all activities in the activities.txt file.
    """
    pass

def validateActivityName(name):
    """
    Takes an activity name and verifies that it exists in the activities file.
    Returns true/false.
    """
    return True
    
def validateTimestamp(timeStamp):
    """
    Takes a user provided timeStamp and verifies that it follows the correct format.
    Returns true/false.
    """
    return True
    
def validateComment(comment):
    """
    Takes a user provided comment and verifies it is valid.
    Returns true/false.
    """
    return True
    
def convertInputToData(timeStamp, comment):
    """
    Takes a correct user timeStamp and comment and converts it to the data folder format.
    Returns string with the correct data folder formatted data.
    """
    pass
    
def writeDataToFile(activityName, data):
    """
    Writes the provided data to the file of the activityName.
    Doesn't return anything.
    """
    pass

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