import os
import sys
import shutil
from codecs import open as codec_open
import settings
from os import  path
  
def ensure_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

def copyFolder (source, dest):
  if (os.path.exists(dest)):
    shutil.rmtree (dest)
  if os.path.exists(source):
    shutil.copytree (source, dest)  
     
def copyStyle (destinationPath): 
  if settings.verbose:
    print ('writing ' + destinationPath + '')
  ensure_dir(destinationPath)
  pathname = os.path.dirname(sys.argv[0])        
  absPath  = os.path.abspath(pathname)
  (parent, app) = os.path.split(absPath)
  sourcePath = parent
  shutil.rmtree (destinationPath)
  shutil.copytree (sourcePath + '/public/style',  destinationPath)
  
def generatePage (fileName, sections):
  if (os.path.isfile(fileName)):
    os.remove(fileName)
  with codec_open(fileName, mode="a", encoding="utf-8") as htmlFile:
    for section in sections:
      htmlFile.write(section)
      
def writePage (path, page):
  (parent, file ) = os.path.split(path) 
  if settings.verbose:
    print ('writing ' + path)
  if (os.path.isfile(path)):
    os.remove(path)  
  ensure_dir(parent)
  with codec_open(path, mode="a", encoding="utf-8") as htmlFile:
    htmlFile.write(page)    
      
      
def read_data_from_file(file_location):
  with codec_open(file_location, mode="r", encoding="utf-8") as f:
    data = f.read()
    return data
  
def getHeadder(fromFile):
  with open(fromFile, 'r') as f:
    first_line = f.readline() 
    title = first_line[1:]
  return title
    
def getIgnoreList():
  if path.isfile('mbignore'): 
    return [word for line in open('mbignore', 'r') for word in line.split()] 
  else:
    return []
     
    
def getContributors():
  contributors = ""
  creditPath = 'credits' 
  if not path.exists(creditPath):  
    creditPath = '../' + creditPath
  if not path.exists(creditPath):  
    creditPath = '../' + creditPath
  if path.exists(creditPath):   
     with open(creditPath, 'r') as f:
       contributors = f.readline()   
  return contributors     

def getAnalyticCode(codeFileName):
  trackingCode = ""
  gaPath = codeFileName 
  if not path.exists(gaPath):  
    gaPath = '../' + gaPath
  if not path.exists(gaPath):  
    gaPath = '../' + gaPath
  if path.exists(gaPath):   
     with open(gaPath, 'r') as f:
       trackingCode = f.readline()   
  trackingCode = trackingCode .replace('\n', '')
  return trackingCode      
  
       
       
       
       
       
       
       