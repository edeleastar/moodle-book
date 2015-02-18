#!/usr/bin/env python
import os

if __name__ == "__main__":
  from os              import path
  from controllers.App import App
  from models.Course   import Course
  from models.Topic    import Topic 
  from models.Book     import Book 
    
  app = App(path.dirname(path.realpath(__file__)))

  if path.exists('course.md'):
    print ('Publishing full course')
    course = Course()
    app.publishCourse(course)
  else:
    if path.exists('topic.md'):
      print ('Publishing topic + contained books')
      fullPath = os.getcwd()
      path, folder = os.path.split(fullPath)
      topic = Topic(folder)
      app.publishTopic(topic)
    else:
      print ('Publishing single book')
      book = Book()
      app.publishLab(book)

