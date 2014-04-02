from os import path
import sys
  
def checkFileExists(expectedFile):
  if not path.exists(expectedFile):
    print ('Cannot find ' + expectedFile + '. Are you in the correct folder (course, topic or book)?')
    sys.exit()