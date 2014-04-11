import unittest
from utils.FileUtils import write
from models.Chapter import Chapter
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


class DefaultWidgetSizeTestCase(unittest.TestCase):
  def runTest(self):
    write ('00.00.md', chapterMd)
    chapter = Chapter('00.00.md')
    self.assertEqual(chapterHtml,  chapter.content)
    self.assertEqual('Objectives\n', chapter.title)
    self.assertEqual(chapterHtmlWithoutHeader,  chapter.contentWithoutHeadder)
    remove ('00.00.md')
    

    
