from utils.FileUtils  import copyFolder, copyStyle
from utils.FileUtils import writePage, getContributors, getAnalyticCode, chunks
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
    tracking = getAnalyticCode('ga')
    content.update({'tracking':tracking})
    content.update({'external':settings.external})
    content.update({'wall':settings.wall})

    writePage(htmlFile, template.render(content))

  def publishLab(self,  book):
    print ('  -->' + book.title)
    bookFolder = os.getcwd()
    topicFolder, bookFolderName  = os.path.split(bookFolder)
    os.chdir(topicFolder)
    fullPath = os.getcwd() 
    path, folder = os.path.split(fullPath)
    topic = Topic(folder)
    os.chdir(bookFolder)
    self.publishLabInTopic(topic, book) 
        
  def publishLabInTopic(self, topic, book):
    print ('  -->' + book.title)
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
    labs = chunks(topic.bookList, 3)
    self.publishPage('topic.html', self.resolveTopicPath(topic) +'/index.html', dict(title=topic.title, course=course, topic=topic, labs=labs))

    topicDir = os.getcwd() 
    for book in topic.bookList:
      os.chdir(topicDir + '/' + book.folder)
      book = Book()
      #self.publishBook(book)
      self.publishLabInTopic(topic, book)    
    
  def publishCourse(self, course):
    copyStyle(self.resolveCoursePath(course) + '/style')
    self.publishPage('course.html', self.resolveCoursePath(course) +'/index.html', dict(course=course))
    courseDir = os.getcwd()
    completeTopics = []
    for topic in course.topicList:
      print ('Writing ' + topic.folder)
      os.chdir(courseDir + '/' + topic.folder)
      topic = Topic(topic.folder)
      completeTopics.append(topic)
      self.publishTopicInCourse(course, topic)
    os.chdir(courseDir);
    if settings.wall:
      allLabs = []
      for topic in completeTopics:
        if topic.bookList:
          allLabs.extend(topic.bookList)
      labs = chunks(allLabs, 3)

      self.publishPage('labwall.html', self.resolveCoursePath(course) +'/labwall.html', dict(course=course, topics=completeTopics, labs=labs))

    
    