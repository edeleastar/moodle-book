#!/usr/bin/env python
if __name__ == "__main__":
  from os              import path
  from controllers.App import App
  from models.Course import Course

  app = App(path.dirname(path.realpath(__file__)))
  course = Course()
  app.publishCourse(course)
  