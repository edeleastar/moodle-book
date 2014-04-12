import unittest
from utils.FileUtils import write
from models.ChapterMd import ChapterMd
from os import remove
from Fixtures import chapterMd, chapterHtml, chapterHtmlWithoutHeader

class ChapterMdTest(unittest.TestCase):
 
  def setUp(self):
    write ('00.00.md', chapterMd)
  def tearDown(self):
    remove ('00.00.md')

  def testMarkdown(self):
    chapter = ChapterMd('00.00.md')
    self.assertEqual(chapterHtml,               chapter.content)
    self.assertEqual('Objectives\n',            chapter.title)
    self.assertEqual ("00",                     chapter.shortTitle)
    self.assertEqual(chapterHtmlWithoutHeader,  chapter.contentWithoutHeadder)

    
