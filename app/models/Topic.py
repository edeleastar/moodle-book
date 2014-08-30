from utils.MarkdownUtils import parse_markdown
from glob import glob
from os import getcwd, path
from utils.FileUtils import getHeadder
from utils.CmdUtils import checkFileExists

class BookSummary:
  def __init__(self, name, objectives):
    self.folder  = name;
    objectivesMd = glob('./' + name + '/0*.md')
    if len(objectivesMd) == 0:
      print ('Cannot locate lab steps in ' + self.folder +  '. Lab steps must be named 0X.XX.md')
      exit()
      
    self.objectives = parse_markdown (objectivesMd[0])
    s = objectivesMd[0]
    s = s[s.find('.')+len('.'):s.rfind('.')]
    self.title = s[s.find('.')+1 :  ]


class Topic:
  def __init__(self):
    checkFileExists ('topic.md')   
    root, self.folder  = path.split(getcwd())
    self.content  = parse_markdown('topic.md')
    self.title    = getHeadder('topic.md')
    self.pdfs = []
    pdfList   = glob('./pdf/*.pdf')
    for pdf in pdfList:
      self.pdfs.append(path.basename(pdf))
    self.bookList = []
    books = glob('./book*')  
    for lab in books:
      self.bookList.append( BookSummary(path.basename(lab), "") )
