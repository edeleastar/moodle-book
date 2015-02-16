from utils.MarkdownUtils import parse_markdown, parse_markdown_without_header
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
    self.contentWithoutHeadder = parse_markdown_without_header (mdFile)
    