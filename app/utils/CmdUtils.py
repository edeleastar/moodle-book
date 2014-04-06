from os import path, getcwd
import sys
  
def checkFileExists(expectedFile):
  if not path.exists(expectedFile):
    print ('Cannot find ' + expectedFile)
    sys.exit()