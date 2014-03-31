from utils.FileUtils  import copyFolder, copyStyle
from utils.FileUtils import writePage
import shutil
import settings 
import os

class Publisher:  

  def resolveBookPath(self, book):
    return '../../' + settings.outputfolder + '/' + book.topic + '/' + book.folderName + '-book'
    
  def resolveSitePath(self, book):
    return '../../' + settings.outputfolder + '/' + book.topic + '/' + book.folderName    

  def resolveTopicPath(self, topic):
    return "../" + settings.outputfolder + '/' + topic.folderName
    
  def remove(self, path):
    if os.path.exists(path):
      shutil.rmtree (path) 

  def copyDirectories(self, book, targetPath):
    for directory in book.directories:
      copyFolder (directory, './' + targetPath + '/'+ directory[2:])
      
  def publishPage(self, template, htmlFile, content):
    template = settings.templateEnv.get_template(template)
    writePage(htmlFile, template.render(content))
 
  def publishBook(self, book):
    self.remove (self.resolveBookPath(book))
    self.copyDirectories(book, self.resolveBookPath(book))
    for chapter in book.chapters:
      self.publishPage('chapter.html', self.resolveBookPath(book) + '/' + chapter.mdFile + '.html',  dict(title=chapter.title, content=chapter.contentWithoutHeadder))  
    shutil.make_archive(self.resolveBookPath(book), format="zip", root_dir = self.resolveBookPath(book))   
    
  def publishLab(self, book):
    self.remove (self.resolveSitePath(book))
    self.copyDirectories(book, self.resolveSitePath(book))
    copyStyle(self.resolveSitePath(book) + '/style')
    self.publishPage('lesson.html',self.resolveSitePath(book) +'/index.html', dict(title=book.title, book=book))
    shutil.make_archive(self.resolveSitePath(book), format="zip", root_dir= self.resolveSitePath(book))   
    
  def publishTopic(self, topic):
    copyStyle(self.resolveTopicPath(topic) + '/style')
    copyFolder ('./pdf', self.resolveTopicPath(topic) + '/pdf')
    self.publishPage('topic.html', self.resolveTopicPath(topic) +'/index.html', dict(title=topic.title, topic=topic))  