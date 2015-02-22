from utils.FileUtils  import copyFolder, copyFile, ensure_dir
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

    writePage(htmlFile, template.render(content))

  def publishLab(self,  book):
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
    self.publishPage('lab.html',self.resolveSitePath(book) +'/index.html', dict(title=book.title, topic=topic, book=book))

  def publishTopic(self, topic):
    topicFolder = os.getcwd()
    courseFolder, topicFolderName  = os.path.split(topicFolder)
    os.chdir(courseFolder)
    course = Course()
    os.chdir(topicFolder)
    self.publishTopicInCourse(course, topic)

  def publishTopicInCourse(self, course, topic):
    ensure_dir(self.resolveTopicPath(topic))
    if topic.topicImg != "none":
      copyFile (topic.topicImg, self.resolveTopicPath(topic) )

    labs  = chunks(topic.bookList, 3)
    talks = chunks(topic.talkList, 3)

    self.publishPage('topic.html',  self.resolveTopicPath(topic) +'/index.html',  dict(course=course, topic=topic, labs=labs, talks=talks))
    self.publishPage('moodle.html', self.resolveTopicPath(topic) +'/moodle.html', dict(course=course, topic=topic, labs=labs, talks=talks))

    topicDir = os.getcwd()

    for talk in topic.talkList:
      copyFolder (talk.name, self.resolveTopicPath(topic) + '/' + talk.name)
    for book in topic.bookList:
      os.chdir(topicDir + '/' + book.name)
      book = Book()
      self.publishLabInTopic(topic, book)

    
  def publishCourse(self, course):
    courseDir = os.getcwd()
    completeTopics = []
    for topic in course.topicList:
      print ('Writing ' + topic.folder)
      os.chdir(courseDir + '/' + topic.folder)
      topic = Topic(topic.folder)
      completeTopics.append(topic)
      self.publishTopicInCourse(course, topic)
    os.chdir(courseDir);
    course.topicList = completeTopics
    self.publishPage('course.html', self.resolveCoursePath(course) +'/index.html', dict(course=course))

    allLabs = []
    for topic in course.topicList:
      if topic.bookList:
        allLabs.extend(topic.bookList)
    labs = chunks(allLabs, 3)
    self.publishPage('wall.html', self.resolveCoursePath(course) +'/labwall.html', dict(course=course, subtitle="Labs", topics=completeTopics, resources=labs, panel_type="panel-danger"))

    allTalks = []
    for topic in course.topicList:
      if topic.talkList:
        allTalks.extend(topic.talkList)
    talks = chunks(allTalks, 3)
    self.publishPage('wall.html', self.resolveCoursePath(course) +'/talkwall.html', dict(course=course, subtitle="Presentations", topics=completeTopics, resources=talks, panel_type="panel-info"))

