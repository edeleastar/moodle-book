from models.Chapter import Chapter
from utils.MarkdownUtils import parse_markdown
from os import remove
from utils.FileUtils import getHeadder

class ChapterMd (Chapter):
  def __init__(self, mdFile):
    Chapter.__init__(self, mdFile)
    self.parse(mdFile)
   
  def parse(self, mdFile):
    self.content = parse_markdown(mdFile)
    self.title   = getHeadder(mdFile)
      
    with open(mdFile, 'r') as fin:
      data = fin.read().splitlines(True)
    with open('temp.md', 'w') as fout:
      fout.writelines(data[1:])
      fout.close()
    self.contentWithoutHeadder  = parse_markdown('temp.md')
    remove ('temp.md')