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
    mdFile = "./pdf/" + name + ".md"
    if (path.isfile(mdFile)):
      self.text = parse_markdown ("./pdf/" + name + ".md")
      self.title = getHeadder("./pdf/" + name + ".md")
      self.textWithoutHeadder = parse_markdown_without_header ("./pdf/" + name + ".md")


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

class Topic:
  def __init__(self, folder):
    checkFileExists ('topic.md')   
    root, self.folder  = path.split(getcwd())
    self.content  = parse_markdown('topic.md')
    self.title    = getHeadder('topic.md')
    self.topicElements = []
    self.topicFolder = folder
    pdfList   = glob('./pdf/*.pdf')
    for pdf in pdfList:
      elementName, type = path.splitext(path.basename(pdf))
      self.topicElements.append(TopicElement(self.topicFolder, elementName))

    self.bookList = []
    books = glob('./book*')  
    for lab in books:
      self.bookList.append( BookSummary(self.topicFolder, path.basename(lab), "") )
