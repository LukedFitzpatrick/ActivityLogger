"""
ActivityLogger 
Luke Fitzpatrick 2014
"""

from loggerFunctions import *

name = getValidatedInput("Activity: ", validateActivityName)
if(name.lower() == "add"):
    addActivity(getValidatedInput("New activity name: ", validateNewActivityName))
else:
    timeStamp = getValidatedInput("Timestamp: ", validateTimestamp)
    comment = getValidatedInput("Comment: ", validateComment)
    writeDataToFile(name, convertInputToData(timeStamp, comment))

 








    