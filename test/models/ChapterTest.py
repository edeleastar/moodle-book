import unittest
from utils.FileUtils import write
from models.ChapterMd import ChapterMd
from os import remove

class ChapterTestTest(unittest.TestCase):
 
  def testShortTitle(self):
    write ('00.Long String.md', 'test')
    chapter = ChapterMd('00.Long String.md')
    self.assertEqual ("Long String", chapter.shortTitle)
    remove ('00.Long String.md')    

  def testBadShortTitle(self):
    write ('00-Long String.md', 'test')
    chapter = ChapterMd('00-Long String.md')
    self.assertEqual ("", chapter.shortTitle)
    remove ('00-Long String.md')
