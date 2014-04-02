from glob import glob
from utils.MarkdownUtils import parse_markdown
from utils.FileUtils import getHeadder, getIgnoreList
from utils.CmdUtils import checkFileExists

class TopicSummary:
  def __init__(self, folder):
    self.folder = folder;
    self.title = getHeadder(folder + '/topic.md')
    
class Course:
  def __init__(self):
    checkFileExists ('course.md')    
    self.content    = parse_markdown('course.md')
    self.title      = getHeadder('course.md')
    ignoreList = getIgnoreList()
    self.topicList  = []
    allTopics  = glob('topic*')
    topicsToPublish = [t for t in allTopics if t not in ignoreList]
    for topic in topicsToPublish:
      self.topicList.append(TopicSummary(topic))  
    