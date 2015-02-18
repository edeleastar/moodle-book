from utils.MarkdownUtils import parse_markdown, parse_markdown_without_header 
from glob import glob
from os import getcwd, path
from utils.FileUtils import getHeadder, getImageFile
from utils.CmdUtils import checkFileExists
from os import remove

class TalkSummary:
  def __init__(self, topicFolder, name):
    self.name = name
    self.topicFolder = topicFolder
    pdfs = glob('./' + name + '/*.pdf')

    if len(pdfs) == 0:
      print ('Cannot locate pdf for talk in ' + self.topicFolder + ": " + name)
      exit()

    self.pdf  = pdfs[0]
    fileName, fileExtension = path.splitext (self.pdf)
    self.img  = getImageFile (fileName)

    if self.img:
      self.fullImgPath = topicFolder + self.img[1:]
      self.fullPdfPath = topicFolder + self.pdf[1:]

    mdFile = fileName + ".md"
    if (path.isfile(mdFile)):
      self.text = parse_markdown (mdFile)
      self.title = getHeadder(mdFile)
      self.textWithoutHeadder = parse_markdown_without_header (mdFile)


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
    self.topicFolder = folder

    self.talkList = []
    talks = glob('./talk*')
    for talk in talks:
      self.talkList.append( TalkSummary(self.topicFolder, path.basename(talk)) )

    self.bookList = []
    books = glob('./book*')  
    for lab in books:
      self.bookList.append( BookSummary(self.topicFolder, path.basename(lab), "") )
