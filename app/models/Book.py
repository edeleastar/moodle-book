from glob import glob
from Chapter import Chapter
from os import walk, getcwd, path

class Book:
  def __init__(self):
    self.mdFiles = glob('*.md')
    self.chapters = []
    self.parseMarkdown()
    folders = [x[0] for x in walk('.')]
    folders.pop(0)
    self.directories = [ folder for folder in folders if not (folder.startswith('./public'))  ]
    root, self.folderName  = path.split(getcwd())
    self.title = self.chapters[0].title
    root, self.topic = path.split(root)

  def parseMarkdown(self): 
    for mdFile in self.mdFiles:
      self.chapters.append (Chapter(mdFile))  
           
