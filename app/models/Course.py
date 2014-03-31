from glob import glob
from utils.MarkdownUtils import parse_markdown
from os import path
import sys


class TopicSummary:
  def __init__(self, folder):
    self.folder = folder;
    with open(folder + '/topic.md', 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
    
class Course:
  def __init__(self):
    if not path.exists('course.md'):
      print ('Cannot find course.md. Are you in the correct folder for the course command?')
      sys.exit()
    
    self.content  = parse_markdown('course.md')
    with open('course.md', 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
    self.topicList = []
    topics  = glob('session*')
    for topic in topics:
      self.topicList.append(TopicSummary(topic))  
    