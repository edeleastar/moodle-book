from Chapter import Chapter


class ChapterQuiz (Chapter):
  def __init__(self, yamlFile):
    Chapter.__init__(self, yamlFile)
    self.title      = 'Quiz Title'
    self.questions = ''
    self.content    = '<script>' + self.questions 
    self.contentWithoutHeadder    = "<p> Quiz <p>"
    
