from glob import glob
from utils.MarkdownUtils import parse_markdown

class TopicSummary:
  def __init__(self, folder):
    self.folder = folder;
    with open(folder + '/index.md', 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
    
class Course:
  def __init__(self):
    self.content  = parse_markdown('index.md')
    with open('index.md', 'r') as f:
      first_line = f.readline() 
      title = first_line[1:]
      self.title = title
    self.topicList = []
    topics  = glob('session*')
    for topic in topics:
      self.topicList.append(TopicSummary(topic))  
    