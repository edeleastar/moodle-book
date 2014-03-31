from utils.MarkdownUtils import parse_markdown
from glob import glob
from os import getcwd, path
import sys

class Lab:
  def __init__(self, name, objectives):
    self.name       = name;
    objectivesMd = glob('./' + name + '/0*.md')
    self.objectives = parse_markdown (objectivesMd[0])

class Topic:
  def __init__(self):
    root, self.folderName  = path.split(getcwd())
    
    if not path.exists('topic.md'):
      print ('Cannot find topic.md. Are you in the correct folder for the topic command?')
      sys.exit()
      
    self.content  = parse_markdown('topic.md')
    with open('topic.md', 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
      self.pdfs = []
      pdfList   = glob('./pdf/*.pdf')
      for pdf in pdfList:
        self.pdfs.append(path.basename(pdf))
      self.labs = []
      labList = glob('./lab*')  
      for lab in labList:
        self.labs.append( Lab(path.basename(lab), "") )
