from glob import glob
from ChapterMd import ChapterMd
from ChapterQuiz import ChapterQuiz
from os import walk, getcwd, path
import sys;

class Book:
  def __init__(self):
    self.mdFiles = glob('*.md')
    self.chapters = []
    self.parseMarkdown()
    folders = [x[0] for x in walk('.')]
    folders.pop(0)
    self.directories = [ folder for folder in folders if not (folder.startswith('./public'))  ]
    root, self.folderName  = path.split(getcwd())
    self.title = self.chapters[0].shortTitle
    root, self.topic = path.split(root)

  def parseMarkdown(self): 
    anyFiles = glob('0*.md')
    if len(anyFiles) == 0:
      print ('Cannot find any markdown files - you must run this command from a course, topic or book folder')
      sys.exit()
    for mdFile in self.mdFiles:
      self.chapters.append (ChapterMd(mdFile))  
