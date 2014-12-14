"""
ActivityLogger 
Luke Fitzpatrick 2014
"""

from loggerFunctions import *

name = getValidatedInput("Activity: ", validateActivityName)
timeStamp = getValidatedInput("Timestamp: ", validateTimestamp)
comment = getValidatedInput("Comment: ", validateComment)

writeDataToFile(name, convertInputToData(timeStamp, comment))

 








    