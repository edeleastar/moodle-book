from glob import glob
from Chapter import Chapter
from os import walk

class Book:
  def __init__(self):
   self.mdFiles = glob('*.md')
   self.chapters = []
   self.parseMarkdown()
   folders = [x[0] for x in walk('.')]
   folders.pop(0)
   self.directories = [ folder for folder in folders if not (folder.startswith('./public'))  ]
   
  def parseMarkdown(self): 
    for mdFile in self.mdFiles:
      self.chapters.append (Chapter(mdFile))  
           
