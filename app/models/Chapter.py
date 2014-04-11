from utils.MarkdownUtils import parse_markdown
from os import remove
import settings
from utils.FileUtils import getHeadder

class Chapter:
  def __init__(self, mdFile):
    self.file = mdFile
    s = self.file
    self.shortTitle  = s[s.find('.')+len('.'):s.rfind('.')] 


    
    