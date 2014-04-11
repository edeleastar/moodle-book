import unittest
from utils.FileUtils import write
from models.ChapterMd import ChapterMd
from os import remove

chapterMd = """#Objectives
- Todo
- Todo
- Todo
""" 
chapterHtml = """<h1>Objectives</h1>
<ul>
<li>Todo</li>
<li>Todo</li>
<li>Todo</li>
</ul>"""

chapterHtmlWithoutHeader = """<ul>
<li>Todo</li>
<li>Todo</li>
<li>Todo</li>
</ul>"""


class basicMdTest(unittest.TestCase):
  def runTest(self):
    write ('00.00.md', chapterMd)
    chapter = ChapterMd('00.00.md')
    self.assertEqual(chapterHtml,               chapter.content)
    self.assertEqual('Objectives\n',            chapter.title)
    self.assertEqual ("00",                      chapter.shortTitle)
    self.assertEqual(chapterHtmlWithoutHeader,  chapter.contentWithoutHeadder)
    remove ('00.00.md')
    
class titleTestCase(unittest.TestCase):
  def runTest(self):
    write ('00.Long String.md', chapterMd)
    chapter = ChapterMd('00.Long String.md')
    self.assertEqual ("Long String", chapter.shortTitle)
    remove ('00.Long String.md')    

class titleIncorrectTestCase(unittest.TestCase):
  def runTest(self):
    write ('00-Long String.md', chapterMd)
    chapter = ChapterMd('00-Long String.md')
    self.assertEqual ("", chapter.shortTitle)
    remove ('00-Long String.md')
