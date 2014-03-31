#!/usr/bin/env python
if __name__ == "__main__":
  from os              import path
  from controllers.App import App
  from models.Topic    import Topic  

  app = App(path.dirname(path.realpath(__file__)))
  topic = Topic()
  app.publishTopic(topic)
  