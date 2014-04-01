from utils.MarkdownUtils import parse_markdown
from os import remove
import settings
from utils.FileUtils import getHeadder

class Chapter:
  def __init__(self, mdFile):
    self.parse(mdFile)
   
  def parse(self, mdFile):
    self.mdFile  = mdFile 
    self.content = parse_markdown(mdFile)
    self.title   = getHeadder(mdFile)

    if not settings.pagetitles:
      s = self.mdFile
      self.title  = s[s.find('.')+len('.'):s.rfind('.')] 
      
    with open(mdFile, 'r') as fin:
      data = fin.read().splitlines(True)
    with open('temp.md', 'w') as fout:
      fout.writelines(data[1:])
      fout.close()
    self.contentWithoutHeadder  = parse_markdown('temp.md')
    remove ('temp.md')   


    
    