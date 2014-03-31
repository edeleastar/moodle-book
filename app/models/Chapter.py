from utils.MarkdownUtils import parse_markdown
from os import remove
import settings

class Chapter:
  def __init__(self, mdFile):
    self.parse(mdFile)
   
  def parse(self, mdFile):
    self.mdFile = mdFile 
    self.content  = parse_markdown(mdFile)
    with open(mdFile, 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
      
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


    
    