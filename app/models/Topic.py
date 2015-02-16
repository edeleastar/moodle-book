from utils.MarkdownUtils import parse_markdown, parse_markdown_without_header 
from glob import glob
from os import getcwd, path
from utils.FileUtils import getHeadder, getImageFile
from utils.CmdUtils import checkFileExists
from os import remove

class TopicElement:
  def __init__(self, topicFolder, name):
    self.name = name
    self.topicFolder = topicFolder
    self.pdf  = name + '.pdf'
    self.img  = getImageFile ('./pdf/' + name)

    if self.img:
      self.fullImgPath = topicFolder + self.img[1:]
      self.fullPdfPath = topicFolder + '/pdf/' + self.pdf

class BookSummary:
  def __init__(self, topicFolder, name, objectives):
    self.topicFolder = topicFolder
    self.folder  = name;
    objectivesMd = glob('./' + name + '/0*.md')
    if len(objectivesMd) == 0:
      print ('Cannot locate lab steps in ' + self.folder +  '. Lab steps must be named 0X.XX.md')
      exit()
      
    self.objectives = parse_markdown (objectivesMd[0])
    self.objectivesWithoutHeadder = parse_markdown_without_header (objectivesMd[0])

    s = objectivesMd[0]
    s = s[s.find('.')+len('.'):s.rfind('.')]
    self.title = s[s.find('.')+1 :  ]
    self.img = getImageFile ('./' + name + '/img/main')  
    if self.img:
      self.fullImgPath = topicFolder + self.img[1:]

class Topic:
  def __init__(self, folder):
    checkFileExists ('topic.md')   
    root, self.folder  = path.split(getcwd())
    self.content  = parse_markdown('topic.md')
    self.contentWithoutHeadder = parse_markdown_without_header ('topic.md')
    self.title    = getHeadder('topic.md')
    self.topicImg = getImageFile ('topic')
    self.topicTest = "test"
    self.topicElements = []
    self.topicFolder = folder

    self.bookList = []
    books = glob('./book*')  
    for lab in books:
      self.bookList.append( BookSummary(self.topicFolder, path.basename(lab), "") )
