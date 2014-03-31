from utils.FileUtils  import copyFolder, copyStyle
from utils.FileUtils import writePage
import shutil
import settings 
import os

class Publisher:  
  def __init__(self):
    self.public = './public'
   
  def copyDirectories(self, book, targetPath):
    for directory in book.directories:
      copyFolder (directory, './' + targetPath + '/'+ directory[2:])
      
  def publishPage(self, template, htmlFile, content):
    template = settings.templateEnv.get_template(template)
    writePage(htmlFile, template.render(content))
 
  def publishBook(self, book):
    if os.path.exists(self.public + '/book'):
      shutil.rmtree (self.public + '/book') 
    self.copyDirectories(book, self.public + '/book')
    for chapter in book.chapters:
      self.publishPage('chapter.html', self.public + '/book/' + chapter.mdFile + '.html',  dict(title=chapter.title, content=chapter.contentWithoutHeadder))  
    shutil.make_archive(self.public + '/book', format="zip", root_dir = self.public + '/book')   

    
  def publishSite(self, book):
    if os.path.exists(self.public + '/site'):
      shutil.rmtree (self.public + '/site') 
    self.copyDirectories(book, self.public + '/site')
    copyStyle(self.public + '/site/style')
    self.publishPage('lesson.html',self.public + '/site/index.html', dict(title="demo", chapters=book.chapters))
    shutil.make_archive(self.public + '/site', format="zip", root_dir= self.public + '/site')   