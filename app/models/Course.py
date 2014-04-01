from glob import glob
from utils.MarkdownUtils import parse_markdown
from utils.FileUtils import getHeadder
from utils.CmdUtils import checkFileExists

class TopicSummary:
  def __init__(self, folder):
    self.folder = folder;
    self.title = getHeadder(folder + '/topic.md')
    
class Course:
  def __init__(self):
    checkFileExists ('course.md', 'course.py')    
    self.content  = parse_markdown('course.md')
    self.title    = getHeadder('course.md')
    self.topicList = []
    topics  = glob('topic*')
    for topic in topics:
      self.topicList.append(TopicSummary(topic))  
    