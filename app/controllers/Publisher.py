from utils.FileUtils  import copyFolder, copyStyle
from utils.FileUtils import writePage
import shutil
import settings 

class Publisher:  
  def __init__(self):
   None
   
  def publishChapter(self, chapter):
    htmlFile = './book/' + chapter.mdFile + '.html'
    template = settings.templateEnv.get_template('chapter.html')
    writePage(htmlFile, template.render(title=chapter.title, content=chapter.contentWithoutHeadder))
 
  def publishBook(self, book):
    for chapter in book.chapters:
      self.publishChapter(chapter) 
    for directory in book.directories:
      copyFolder (directory, './book/'+ directory[2:])
    shutil.make_archive('book', format="zip", root_dir='./book')   
    shutil.rmtree ('./book') 
    
  def publishLesson(self, book):
    for directory in book.directories:
      copyFolder (directory, './site/'+ directory[2:])
    copyStyle('./site/style')
    htmlFile = './site/index.html'
    template = settings.templateEnv.get_template('lesson.html')
    writePage(htmlFile, template.render(title="demo", chapters=book.chapters))
    shutil.make_archive('site', format="zip", root_dir='./site')   