from utils.MarkdownUtils import parse_markdown
from os import remove
import settings
from utils.FileUtils import getHeadder

class Chapter:
  def __init__(self, mdFile):
    self.file = mdFile
    s = self.file
    self.shortTitle  = s[s.find('.')+len('.'):s.rfind('.')] 
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
    
    