from utils.MarkdownUtils import parse_markdown
from glob import glob
from os import getcwd, path
from utils.FileUtils import getHeadder, getImageFile
from utils.CmdUtils import checkFileExists

class TopicElement:
  def __init__(self, name):
    self.pdf  = name + '.pdf'
    self.img  = getImageFile ('./pdf/' + name)
    mdFile = "./pdf/" + name + ".md"
    if (path.isfile(mdFile)):
      self.text = parse_markdown ("./pdf/" + name + ".md")


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
    self.img = getImageFile ('./' + name + '/img/main')  

class Topic:
  def __init__(self):
    checkFileExists ('topic.md')   
    root, self.folder  = path.split(getcwd())
    self.content  = parse_markdown('topic.md')
    self.title    = getHeadder('topic.md')
    self.topicElements = []
    pdfList   = glob('./pdf/*.pdf')
    for pdf in pdfList:
      elementName, type = path.splitext(path.basename(pdf))
      self.topicElements.append(TopicElement(elementName))

    self.bookList = []
    books = glob('./book*')  
    for lab in books:
      self.bookList.append( BookSummary(path.basename(lab), "") )
