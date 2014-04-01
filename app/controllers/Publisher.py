from utils.FileUtils  import copyFolder, copyStyle
from utils.FileUtils import writePage, getContributors
import shutil
import settings 
import os
from models.Topic    import Topic  
from models.Book     import Book  
from models.Course   import Course 

class Publisher:  

  def resolveBookPath(self, book):
    return '../../' + settings.outputfolder + '/' + book.topic + '/' + book.folderName + '-moodle'
    
  def resolveSitePath(self, book):
    return '../../' + settings.outputfolder + '/' + book.topic + '/' + book.folderName    

  def resolveTopicPath(self, topic):
    return "../" + settings.outputfolder + '/' + topic.folder
  
  def resolveCoursePath(self, topic):
    return "./" + settings.outputfolder
   
  def remove(self, path):
    if os.path.exists(path):
      shutil.rmtree (path) 

  def copyDirectories(self, book, targetPath):
    for directory in book.directories:
      copyFolder (directory, './' + targetPath + '/'+ directory[2:])
      
  def publishPage(self, template, htmlFile, content):
    template = settings.templateEnv.get_template(template)
    content.update ({'contributors':getContributors()})
    writePage(htmlFile, template.render(content))
 
  def publishBook(self, book):
    print ('  -->' + book.title)
    self.remove (self.resolveBookPath(book))
    self.copyDirectories(book, self.resolveBookPath(book))
    for chapter in book.chapters:
      self.publishPage('chapter.html', self.resolveBookPath(book) + '/' + chapter.mdFile + '.html',  dict(title=chapter.title, content=chapter.contentWithoutHeadder))  
    shutil.make_archive(self.resolveBookPath(book), format="zip", root_dir = self.resolveBookPath(book))   
    shutil.rmtree(self.resolveBookPath(book));

  def publishLab(self,  book):
    bookFolder = os.getcwd()
    topicFolder, bookFolderName  = os.path.split(bookFolder)
    os.chdir(topicFolder)
    topic = Topic()
    os.chdir(bookFolder)
    self.publishLabInTopic(topic, book) 
        
  def publishLabInTopic(self, topic, book):
    self.remove (self.resolveSitePath(book))
    self.copyDirectories(book, self.resolveSitePath(book))
    copyStyle(self.resolveSitePath(book) + '/style')
    self.publishPage('lab.html',self.resolveSitePath(book) +'/index.html', dict(title=book.title, topic=topic, book=book))
    shutil.make_archive(self.resolveSitePath(book) + '-archive', format="zip", root_dir= self.resolveSitePath(book))   
    
  def publishTopic(self, topic):
    topicFolder = os.getcwd()
    courseFolder, topicFolderName  = os.path.split(topicFolder)
    os.chdir(courseFolder)
    course = Course()
    os.chdir(topicFolder)
    self.publishTopicInCourse(course, topic)
    
  def publishTopicInCourse(self, course, topic):
    copyStyle(self.resolveTopicPath(topic) + '/style')
    copyFolder ('./pdf', self.resolveTopicPath(topic) + '/pdf')
    self.publishPage('topic.html', self.resolveTopicPath(topic) +'/index.html', dict(title=topic.title, course=course, topic=topic)) 
    topicDir = os.getcwd() 
    for book in topic.bookList:
      os.chdir(topicDir + '/' + book.folder)
      book = Book()
      self.publishBook(book)
      self.publishLabInTopic(topic, book)    
    
  def publishCourse(self, course):
    copyStyle(self.resolveCoursePath(course) + '/style')
    self.publishPage('course.html', self.resolveCoursePath(course) +'/index.html', dict(course=course))
    courseDir = os.getcwd()
    for topic in course.topicList:
      print ('Writing ' + topic.folder)
      os.chdir(courseDir + '/' + topic.folder)
      topic = Topic()
      self.publishTopicInCourse(course, topic)
      
    
    
    