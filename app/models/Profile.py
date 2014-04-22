from utils.MarkdownUtils import parse_markdown
from os import remove
from utils.FileUtils import getHeadder
from utils.CmdUtils import checkFileExists

class Profile:
  def __init__(self):
    mdFile = 'profile.md'
    checkFileExists (mdFile)  
    self.title   = getHeadder(mdFile)
      
    with open(mdFile, 'r') as fin:
      data = fin.read().splitlines(True)
    with open('temp.md', 'w') as fout:
      fout.writelines(data[1:])
      fout.close()
    self.content = parse_markdown('temp.md')
    remove ('temp.md')

