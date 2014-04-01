from os import path
import sys
  
def checkFileExists(expectedFile, command):
  if not path.exists(expectedFile):
    print ('Cannot find ' + expectedFile + '. Are you in the correct folder for the ' + command + ' command?')
    sys.exit()